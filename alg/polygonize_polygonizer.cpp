/******************************************************************************
 * Project:  GDAL
 * Purpose:  Implements The Two-Arm Chains EdgeTracing Algorithm
 * Author:   kikitte.lee
 *
 ******************************************************************************
 * Copyright (c) 2023, kikitte.lee <kikitte.lee@gmail.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 ****************************************************************************/

/*! @cond Doxygen_Suppress */

#include "polygonize_polygonizer.h"

#include <algorithm>

RPolygon::~RPolygon()
{
    for (auto &arc : oArcs)
    {
        delete arc;
    }
}

IndexedArc RPolygon::newArc(bool bFollowRighthand)
{
    Arc *poArc = new Arc();
    std::size_t iArcIndex = oArcs.size();
    oArcs.push_back(poArc);
    oArcRighthandFollow.push_back(bFollowRighthand);
    oArcConnections.push_back(iArcIndex);
    return IndexedArc{poArc, iArcIndex};
}

void RPolygon::setArcConnection(IndexedArc &oArc, IndexedArc &oNextArc)
{
    oArcConnections[oArc.iIndex] = oNextArc.iIndex;
}

void RPolygon::updateBottomRightPos(IndexType iRow, IndexType iCol)
{
    iBottomRightRow = iRow;
    iBottomRightCol = iCol;
}

void ProcessArmConnections(TwoArm *poCurrent, TwoArm *poAbove, TwoArm *poLeft)
{
    poCurrent->poPolyInside->updateBottomRightPos(poCurrent->iRow,
                                                  poCurrent->iCol);
    poCurrent->bSolidVertical = poCurrent->poPolyInside != poLeft->poPolyInside;
    poCurrent->bSolidHorizontal =
        poCurrent->poPolyInside != poAbove->poPolyInside;
    poCurrent->poPolyAbove = poAbove->poPolyInside;
    poCurrent->poPolyLeft = poLeft->poPolyInside;

    int nArmConnectionType =
        (static_cast<int>(poAbove->bSolidVertical) << 3) |
        (static_cast<int>(poLeft->bSolidHorizontal) << 2) |
        (static_cast<int>(poCurrent->bSolidVertical) << 1) |
        static_cast<int>(poCurrent->bSolidHorizontal);

    /**
     * There are 12 valid connection types depending on the arm types(virtual or solid)
     * The following diagram illustrates these kinds of connection types, ⇢⇣ means virtual arm, →↓ means solid arm.
     *     ⇣        ⇣          ⇣         ⇣        ↓
     *    ⇢ →      → →        → ⇢       → →      ⇢ →
     *     ↓        ⇣          ↓         ↓        ⇣
     *   type=3    type=5    type=6    type=7    type=9
     *
     *     ↓        ↓          ↓         ↓          ↓
     *    ⇢ ⇢      ⇢ →        → ⇢       → →        → ⇢
     *     ↓        ↓          ⇣         ⇣          ↓
     *   type=10  type=11    type=12    type=13   type=14
     *
     *     ↓        ⇣
     *    → →      ⇢ ⇢
     *     ↓        ⇣
     *   type=15  type=0
     *
     *   For each connection type, we may create new arc, ,
     *   Depending on the connection type, we may do the following things:
     *       1. Create new arc. If the arc is closed to the inner polygon, it is called "Inner Arc", otherwise "Outer Arc"
     *       2. Pass an arc to the next arm.
     *       3. "Close" two arcs. If two arcs meet at the bottom right corner of a cell, close them by recording the arc connection.
     *       4. Add grid position(row, col) to an arc.
     */

    switch (nArmConnectionType)
    {
        case 0:
            // nothing to do
            break;

        case 3:
            // add inner arcs
            poCurrent->oArcVerInner = poCurrent->poPolyInside->newArc(true);
            poCurrent->oArcHorInner = poCurrent->poPolyInside->newArc(false);
            poCurrent->poPolyInside->setArcConnection(poCurrent->oArcHorInner,
                                                      poCurrent->oArcVerInner);
            poCurrent->oArcVerInner.poArc->emplace_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            // add outer arcs
            poCurrent->oArcHorOuter = poAbove->poPolyInside->newArc(true);
            poCurrent->oArcVerOuter = poAbove->poPolyInside->newArc(false);
            poAbove->poPolyInside->setArcConnection(poCurrent->oArcVerOuter,
                                                    poCurrent->oArcHorOuter);
            poCurrent->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 5:
            // pass arcs
            poCurrent->oArcHorInner = poLeft->oArcHorInner;
            poCurrent->oArcHorOuter = poLeft->oArcHorOuter;

            break;
        case 6:
            // pass arcs
            poCurrent->oArcVerInner = poLeft->oArcHorOuter;
            poCurrent->oArcVerOuter = poLeft->oArcHorInner;
            poCurrent->oArcVerInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poCurrent->oArcVerOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 7:
            // pass arcs
            poCurrent->oArcHorOuter = poLeft->oArcHorOuter;
            poCurrent->oArcVerOuter = poLeft->oArcHorInner;
            poLeft->oArcHorInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            // add inner arcs
            poCurrent->oArcVerInner = poCurrent->poPolyInside->newArc(true);
            poCurrent->oArcHorInner = poCurrent->poPolyInside->newArc(false);
            poCurrent->poPolyInside->setArcConnection(poCurrent->oArcHorInner,
                                                      poCurrent->oArcVerInner);
            poCurrent->oArcVerInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 9:
            // pass arcs
            poCurrent->oArcHorOuter = poAbove->oArcVerInner;
            poCurrent->oArcHorInner = poAbove->oArcVerOuter;
            poCurrent->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poCurrent->oArcHorInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 10:
            // pass arcs
            poCurrent->oArcVerInner = poAbove->oArcVerInner;
            poCurrent->oArcVerOuter = poAbove->oArcVerOuter;

            break;
        case 11:
            // pass arcs
            poCurrent->oArcHorOuter = poAbove->oArcVerInner;
            poCurrent->oArcVerOuter = poAbove->oArcVerOuter;
            poCurrent->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            // add inner arcs
            poCurrent->oArcVerInner = poCurrent->poPolyInside->newArc(true);
            poCurrent->oArcHorInner = poCurrent->poPolyInside->newArc(false);
            poCurrent->poPolyInside->setArcConnection(poCurrent->oArcHorInner,
                                                      poCurrent->oArcVerInner);
            poCurrent->oArcVerInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 12:
            // close arcs
            poLeft->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poLeft->poPolyAbove->setArcConnection(poLeft->oArcHorOuter,
                                                  poAbove->oArcVerOuter);
            // close arcs
            poAbove->oArcVerInner.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poCurrent->poPolyInside->setArcConnection(poAbove->oArcVerInner,
                                                      poLeft->oArcHorInner);

            break;
        case 13:
            // close arcs
            poLeft->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poLeft->poPolyAbove->setArcConnection(poLeft->oArcHorOuter,
                                                  poAbove->oArcVerOuter);
            // pass arcs
            poCurrent->oArcHorOuter = poAbove->oArcVerInner;
            poCurrent->oArcHorInner = poLeft->oArcHorInner;
            poCurrent->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 14:
            // close arcs
            poLeft->oArcHorOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});
            poLeft->poPolyAbove->setArcConnection(poLeft->oArcHorOuter,
                                                  poAbove->oArcVerOuter);
            // pass arcs
            poCurrent->oArcVerInner = poAbove->oArcVerInner;
            poCurrent->oArcVerOuter = poLeft->oArcHorInner;
            poCurrent->oArcVerOuter.poArc->push_back(
                Point{poCurrent->iRow, poCurrent->iCol});

            break;
        case 15:
            // Tow pixels of the main diagonal belong to the same polygon
            if (poAbove->poPolyLeft == poCurrent->poPolyInside)
            {
                // pass arcs
                poCurrent->oArcVerInner = poLeft->oArcHorOuter;
                poCurrent->oArcHorInner = poAbove->oArcVerOuter;
                poCurrent->oArcVerInner.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
                poCurrent->oArcHorInner.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
            }
            else
            {
                // close arcs
                poLeft->oArcHorOuter.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
                poLeft->poPolyAbove->setArcConnection(poLeft->oArcHorOuter,
                                                      poAbove->oArcVerOuter);
                // add inner arcs
                poCurrent->oArcVerInner = poCurrent->poPolyInside->newArc(true);
                poCurrent->oArcHorInner =
                    poCurrent->poPolyInside->newArc(false);
                poCurrent->poPolyInside->setArcConnection(
                    poCurrent->oArcHorInner, poCurrent->oArcVerInner);
                poCurrent->oArcVerInner.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
            }

            // Tow pixels of the secondary diagonal belong to the same polygon
            if (poAbove->poPolyInside == poLeft->poPolyInside)
            {
                // close arcs
                poAbove->poPolyInside->setArcConnection(poAbove->oArcVerInner,
                                                        poLeft->oArcHorInner);
                poAbove->oArcVerInner.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
                // add outer arcs
                poCurrent->oArcHorOuter = poAbove->poPolyInside->newArc(true);
                poCurrent->oArcVerOuter = poAbove->poPolyInside->newArc(false);
                poCurrent->oArcHorOuter.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
                poAbove->poPolyInside->setArcConnection(
                    poCurrent->oArcVerOuter, poCurrent->oArcHorOuter);
            }
            else
            {
                // pass arcs
                poCurrent->oArcHorOuter = poAbove->oArcVerInner;
                poCurrent->oArcVerOuter = poLeft->oArcHorInner;
                poCurrent->oArcHorOuter.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
                poCurrent->oArcVerOuter.poArc->push_back(
                    Point{poCurrent->iRow, poCurrent->iCol});
            }

            break;

        default:
            // Impossible case
            CPLAssert(false);
            break;
    }
}

template <typename PolyIdType, typename DataType>
Polygonizer<PolyIdType, DataType>::Polygonizer(
    PolygonReceiver<DataType> *poPolygonReceiver)
    : poPolygonReceiver_(poPolygonReceiver)
{
    poTheOuterPolygon_ = createPolygon(THE_OUTER_POLYGON_ID);
}

template <typename PolyIdType, typename DataType>
Polygonizer<PolyIdType, DataType>::~Polygonizer()
{
    for (auto &pair : oPolygonMap_)
    {
        delete pair.second;
    }
}

template <typename PolyIdType, typename DataType>
RPolygon *Polygonizer<PolyIdType, DataType>::getPolygon(PolyIdType nPolygonId)
{
    if (oPolygonMap_.count(nPolygonId) == 0)
    {
        return createPolygon(nPolygonId);
    }
    else
    {
        return oPolygonMap_[nPolygonId];
    }
}

template <typename PolyIdType, typename DataType>
RPolygon *
Polygonizer<PolyIdType, DataType>::createPolygon(PolyIdType nPolygonId)
{
    auto polygon = new RPolygon();
    oPolygonMap_[nPolygonId] = polygon;
    return polygon;
}

template <typename PolyIdType, typename DataType>
void Polygonizer<PolyIdType, DataType>::destroyPolygon(PolyIdType nPolygonId)
{
    delete oPolygonMap_[nPolygonId];
    oPolygonMap_.erase(nPolygonId);
}

template <typename PolyIdType, typename DataType>
void Polygonizer<PolyIdType, DataType>::processLine(
    const PolyIdType *panThisLineId, const DataType *panLastLineVal,
    const GByte *pabyLastLineValMask, TwoArm *poThisLineArm,
    TwoArm *poLastLineArm, const IndexType nCurrentRow, const IndexType nCols)
{
    TwoArm *poCurrent, *poAbove, *poLeft;

    poCurrent = poThisLineArm + 1;
    poCurrent->iRow = nCurrentRow;
    poCurrent->iCol = 0;
    poCurrent->poPolyInside = getPolygon(panThisLineId[0]);
    poAbove = poLastLineArm + 1;
    poLeft = poThisLineArm;
    poLeft->poPolyInside = poTheOuterPolygon_;
    ProcessArmConnections(poCurrent, poAbove, poLeft);
    for (IndexType col = 1; col < nCols; ++col)
    {
        IndexType iArmIndex = col + 1;
        poCurrent = poThisLineArm + iArmIndex;
        poCurrent->iRow = nCurrentRow;
        poCurrent->iCol = col;
        poCurrent->poPolyInside = getPolygon(panThisLineId[col]);
        poAbove = poLastLineArm + iArmIndex;
        poLeft = poThisLineArm + iArmIndex - 1;
        ProcessArmConnections(poCurrent, poAbove, poLeft);
    }
    poCurrent = poThisLineArm + nCols + 1;
    poCurrent->iRow = nCurrentRow;
    poCurrent->iCol = nCols;
    poCurrent->poPolyInside = poTheOuterPolygon_;
    poAbove = poLastLineArm + nCols + 1;
    poAbove->poPolyInside = poTheOuterPolygon_;
    poLeft = poThisLineArm + nCols;
    ProcessArmConnections(poCurrent, poAbove, poLeft);

    /**
     *
     * Find those polygons haven't been processed on this line as we can be sure they are completed
     *
     */
    std::vector<PolygonMapEntry> oCompletedPolygons;
    for (auto &entry : oPolygonMap_)
    {
        RPolygon *poPolygon = entry.second;

        if (poPolygon->iBottomRightRow == nCurrentRow - 1)
        {
            oCompletedPolygons.push_back(entry);
        }
    }
    for (auto &entry : oCompletedPolygons)
    {
        PolyIdType nPolyId = entry.first;
        RPolygon *poPolygon = entry.second;

        // emit valid polygon only
        if (pabyLastLineValMask[poPolygon->iBottomRightCol])
        {
            poPolygonReceiver_->receive(
                poPolygon, panLastLineVal[poPolygon->iBottomRightCol]);
        }

        destroyPolygon(nPolyId);
    }
}

template <typename DataType>
OGRPolygonWriter<DataType>::OGRPolygonWriter(OGRLayerH hOutLayer,
                                             int iPixValField,
                                             double *padfGeoTransform)
    : PolygonReceiver<DataType>(), hOutLayer_(hOutLayer),
      iPixValField_(iPixValField), padfGeoTransform_(padfGeoTransform)
{
}

template <typename DataType>
void OGRPolygonWriter<DataType>::receive(RPolygon *poPolygon,
                                         DataType nPolygonCellValue)
{
    std::vector<bool> oAccessedArc(poPolygon->oArcConnections.size(), false);
    double *padfGeoTransform = padfGeoTransform_;

    OGRGeometryH hPolygon = OGR_G_CreateGeometry(wkbPolygon);

    auto AddRingToPolygon = [&poPolygon, &oAccessedArc, &hPolygon,
                             padfGeoTransform](std::size_t iFirstArcIndex)
    {
        OGRGeometryH hRing = OGR_G_CreateGeometry(wkbLinearRing);

        auto AddArcToRing =
            [&poPolygon, &hRing, padfGeoTransform](std::size_t iArcIndex)
        {
            auto oArc = poPolygon->oArcs[iArcIndex];
            bool bArcFollowRighthand =
                poPolygon->oArcRighthandFollow[iArcIndex];
            for (std::size_t i = 0; i < oArc->size(); ++i)
            {
                Point &oPixel =
                    (*oArc)[bArcFollowRighthand ? i : (oArc->size() - i - 1)];

                const double dfX = padfGeoTransform[0] +
                                   oPixel[1] * padfGeoTransform[1] +
                                   oPixel[0] * padfGeoTransform[2];
                const double dfY = padfGeoTransform[3] +
                                   oPixel[1] * padfGeoTransform[4] +
                                   oPixel[0] * padfGeoTransform[5];

                OGR_G_AddPoint_2D(hRing, dfX, dfY);
            }
        };

        AddArcToRing(iFirstArcIndex);

        std::size_t iArcIndex = iFirstArcIndex;
        std::size_t iNextArcIndex = poPolygon->oArcConnections[iArcIndex];
        oAccessedArc[iArcIndex] = true;
        while (iNextArcIndex != iFirstArcIndex)
        {
            AddArcToRing(iNextArcIndex);
            iArcIndex = iNextArcIndex;
            iNextArcIndex = poPolygon->oArcConnections[iArcIndex];
            oAccessedArc[iArcIndex] = true;
        }

        // close ring manually
        OGR_G_AddPoint_2D(hRing, OGR_G_GetX(hRing, 0), OGR_G_GetY(hRing, 0));

        OGR_G_AddGeometryDirectly(hPolygon, hRing);
    };

    std::vector<bool>::iterator ite;
    while ((ite = std::find_if_not(oAccessedArc.begin(), oAccessedArc.end(),
                                   [](bool accessed) { return accessed; })) !=
           oAccessedArc.end())
    {
        AddRingToPolygon(ite - oAccessedArc.begin());
    }

    // Create the feature object
    OGRFeatureH hFeat = OGR_F_Create(OGR_L_GetLayerDefn(hOutLayer_));

    OGR_F_SetGeometryDirectly(hFeat, hPolygon);

    if (iPixValField_ >= 0)
        OGR_F_SetFieldDouble(hFeat, iPixValField_,
                             static_cast<double>(nPolygonCellValue));

    // Write the to the layer.
    if (OGR_L_CreateFeature(hOutLayer_, hFeat) != OGRERR_NONE)
        eErr_ = CE_Failure;

    OGR_F_Destroy(hFeat);
}

/*! @endcond */
