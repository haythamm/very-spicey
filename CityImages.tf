KPL/FK
 
   FILE: CityImages.tf
 
   This file was created by PINPOINT.
 
   PINPOINT Version 3.2.0 --- September 6, 2016
   PINPOINT RUN DATE/TIME:    2017-09-24T15:45:12
   PINPOINT DEFINITIONS FILE: CityImage.setup
   PINPOINT PCK FILE:         pck00010.tpc
   PINPOINT SPK FILE:         CityImages.bsp
 
   The input definitions file is appended to this
   file as a comment block.
 
 
   Body-name mapping follows:
 
\begindata
 
   NAIF_BODY_NAME                      += 'ASU-GS'
   NAIF_BODY_CODE                      += -9999999
 
   NAIF_BODY_NAME                      += 'LA-00'
   NAIF_BODY_CODE                      += -1111111
 
   NAIF_BODY_NAME                      += 'CH-00'
   NAIF_BODY_CODE                      += -2222222
 
   NAIF_BODY_NAME                      += 'HO-00'
   NAIF_BODY_CODE                      += -3333333
 
   NAIF_BODY_NAME                      += 'BA-00'
   NAIF_BODY_CODE                      += -4444444
 
   NAIF_BODY_NAME                      += 'AT-00'
   NAIF_BODY_CODE                      += -5555555
 
   NAIF_BODY_NAME                      += 'MI-00'
   NAIF_BODY_CODE                      += -6666666
 
\begintext
 
 
   Reference frame specifications follow:
 
 
   Topocentric frame ASU-GS_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame ASU-GS_TOPO is centered at the
      site ASU-GS, which has Cartesian coordinates
 
         X (km):                 -0.1990266286716E+04
         Y (km):                 -0.4943840215933E+04
         Z (km):                  0.3492963086147E+04
 
      and planetodetic coordinates
 
         Longitude (deg):      -111.9284813200000
         Latitude  (deg):        33.4179609000000
         Altitude   (km):         0.4000000000002E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_ASU-GS_TOPO                   =  -8999999
   FRAME_-8999999_NAME                 =  'ASU-GS_TOPO'
   FRAME_-8999999_CLASS                =  4
   FRAME_-8999999_CLASS_ID             =  -8999999
   FRAME_-8999999_CENTER               =  -9999999
 
   OBJECT_-9999999_FRAME               =  'ASU-GS_TOPO'
 
   TKFRAME_-8999999_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-8999999_SPEC               =  'ANGLES'
   TKFRAME_-8999999_UNITS              =  'DEGREES'
   TKFRAME_-8999999_AXES               =  ( 3, 2, 3 )
   TKFRAME_-8999999_ANGLES             =  ( -248.0715186800000,
                                             -56.5820391000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame LA-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame LA-00_TOPO is centered at the
      site LA-00, which has Cartesian coordinates
 
         X (km):                 -0.2503384994510E+04
         Y (km):                 -0.4660254967371E+04
         Z (km):                  0.3551284878185E+04
 
      and planetodetic coordinates
 
         Longitude (deg):      -118.2437000000000
         Latitude  (deg):        34.0522000000000
         Altitude   (km):         0.7100000000194E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_LA-00_TOPO                    =  -111111
   FRAME_-111111_NAME                  =  'LA-00_TOPO'
   FRAME_-111111_CLASS                 =  4
   FRAME_-111111_CLASS_ID              =  -111111
   FRAME_-111111_CENTER                =  -1111111
 
   OBJECT_-1111111_FRAME               =  'LA-00_TOPO'
 
   TKFRAME_-111111_RELATIVE            =  'IAU_EARTH'
   TKFRAME_-111111_SPEC                =  'ANGLES'
   TKFRAME_-111111_UNITS               =  'DEGREES'
   TKFRAME_-111111_AXES                =  ( 3, 2, 3 )
   TKFRAME_-111111_ANGLES              =  ( -241.7563000000000,
                                             -55.9478000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame CH-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame CH-00_TOPO is centered at the
      site CH-00, which has Cartesian coordinates
 
         X (km):                  0.1966966675066E+03
         Y (km):                 -0.4752113517727E+04
         Z (km):                  0.4235652800659E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -87.6298000000000
         Latitude  (deg):        41.8781000000000
         Altitude   (km):         0.1810000000006E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_CH-00_TOPO                    =  -1222222
   FRAME_-1222222_NAME                 =  'CH-00_TOPO'
   FRAME_-1222222_CLASS                =  4
   FRAME_-1222222_CLASS_ID             =  -1222222
   FRAME_-1222222_CENTER               =  -2222222
 
   OBJECT_-2222222_FRAME               =  'CH-00_TOPO'
 
   TKFRAME_-1222222_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-1222222_SPEC               =  'ANGLES'
   TKFRAME_-1222222_UNITS              =  'DEGREES'
   TKFRAME_-1222222_AXES               =  ( 3, 2, 3 )
   TKFRAME_-1222222_ANGLES             =  ( -272.3702000000000,
                                             -48.1219000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame HO-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame HO-00_TOPO is centered at the
      site HO-00, which has Cartesian coordinates
 
         X (km):                 -0.5185940736548E+03
         Y (km):                 -0.5517189577988E+04
         Z (km):                  0.3147356308888E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -95.3698000000000
         Latitude  (deg):        29.7604000000000
         Altitude   (km):         0.2400000000029E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_HO-00_TOPO                    =  -2333333
   FRAME_-2333333_NAME                 =  'HO-00_TOPO'
   FRAME_-2333333_CLASS                =  4
   FRAME_-2333333_CLASS_ID             =  -2333333
   FRAME_-2333333_CENTER               =  -3333333
 
   OBJECT_-3333333_FRAME               =  'HO-00_TOPO'
 
   TKFRAME_-2333333_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-2333333_SPEC               =  'ANGLES'
   TKFRAME_-2333333_UNITS              =  'DEGREES'
   TKFRAME_-2333333_AXES               =  ( 3, 2, 3 )
   TKFRAME_-2333333_ANGLES             =  ( -264.6302000000000,
                                             -60.2396000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame BA-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame BA-00_TOPO is centered at the
      site BA-00, which has Cartesian coordinates
 
         X (km):                  0.1144526265443E+04
         Y (km):                 -0.4808760116700E+04
         Z (km):                  0.4017412638478E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -76.6122000000000
         Latitude  (deg):        39.2904000000000
         Altitude   (km):         0.1460000000017E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_BA-00_TOPO                    =  -3444444
   FRAME_-3444444_NAME                 =  'BA-00_TOPO'
   FRAME_-3444444_CLASS                =  4
   FRAME_-3444444_CLASS_ID             =  -3444444
   FRAME_-3444444_CENTER               =  -4444444
 
   OBJECT_-4444444_FRAME               =  'BA-00_TOPO'
 
   TKFRAME_-3444444_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-3444444_SPEC               =  'ANGLES'
   TKFRAME_-3444444_UNITS              =  'DEGREES'
   TKFRAME_-3444444_AXES               =  ( 3, 2, 3 )
   TKFRAME_-3444444_ANGLES             =  ( -283.3878000000000,
                                             -50.7096000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame AT-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame AT-00_TOPO is centered at the
      site AT-00, which has Cartesian coordinates
 
         X (km):                  0.5191783120025E+03
         Y (km):                 -0.5283595381148E+04
         Z (km):                  0.3523508885059E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -84.3880000000000
         Latitude  (deg):        33.7490000000000
         Altitude   (km):         0.3200000000006E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_AT-00_TOPO                    =  -4555555
   FRAME_-4555555_NAME                 =  'AT-00_TOPO'
   FRAME_-4555555_CLASS                =  4
   FRAME_-4555555_CLASS_ID             =  -4555555
   FRAME_-4555555_CENTER               =  -5555555
 
   OBJECT_-5555555_FRAME               =  'AT-00_TOPO'
 
   TKFRAME_-4555555_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-4555555_SPEC               =  'ANGLES'
   TKFRAME_-4555555_UNITS              =  'DEGREES'
   TKFRAME_-4555555_AXES               =  ( 3, 2, 3 )
   TKFRAME_-4555555_ANGLES             =  ( -275.6120000000000,
                                             -56.2510000000000,
                                             180.0000000000000 )
 
 
\begintext
 
   Topocentric frame MI-00_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame MI-00_TOPO is centered at the
      site MI-00, which has Cartesian coordinates
 
         X (km):                 -0.2574051269575E+03
         Y (km):                 -0.4512177647082E+04
         Z (km):                  0.4485782084059E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -93.2650000000000
         Latitude  (deg):        44.9778000000000
         Altitude   (km):         0.2530000000007E+00
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781366000000E+03
         Polar radius      (km):  6.3567519000000E+03
 
      All of the above coordinates are relative to the frame IAU_EARTH.
 
 
\begindata
 
   FRAME_MI-00_TOPO                    =  -5666666
   FRAME_-5666666_NAME                 =  'MI-00_TOPO'
   FRAME_-5666666_CLASS                =  4
   FRAME_-5666666_CLASS_ID             =  -5666666
   FRAME_-5666666_CENTER               =  -6666666
 
   OBJECT_-6666666_FRAME               =  'MI-00_TOPO'
 
   TKFRAME_-5666666_RELATIVE           =  'IAU_EARTH'
   TKFRAME_-5666666_SPEC               =  'ANGLES'
   TKFRAME_-5666666_UNITS              =  'DEGREES'
   TKFRAME_-5666666_AXES               =  ( 3, 2, 3 )
   TKFRAME_-5666666_ANGLES             =  ( -266.7350000000000,
                                             -45.0222000000000,
                                             180.0000000000000 )
 
\begintext
 
 
Definitions file CityImage.setup
--------------------------------------------------------------------------------
 
begintext
    Developer: Jeremy Jakubowski
Core Cities to Image:
Phoenix
Los Angeles
Chicago
Houston
Baltimore
Atlanta
Minneapolos
 
Support Cities to Image:
Jacksonville
Las Vegas
Albuquerque
Boston
San Francisco
Charlotte
Salt Lake City
OKlahoma City
Memphis
New Orleans
    The ASU Ground Station XYZ location was generated using:
        http://www.apsalin.com/convert-geodetic-to-cartesian.aspx
 
    The calculations was done using the WGS-84 method and the parameters used were:
        Lattitude: 33.4179609
        Longitude: -111.92848132
 
    The TOPO angles used in the ASU-GS_TOPO frame were generated following the instrutions here:
        https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/fk/earth_topo_050714.tf
 
    TOPO Angles:
 
    The orientation of a topocentric frame relative to the base frame can
    be described by an Euler angle sequence.  Let M be the rotation
    matrix that maps vectors from the base frame to a specified
    topocentric frame.  Then
 
        M   =  [ Pi  ]  [ Pi/2 - LAT ]  [ LON ]
                    3               2        3
 
    where LON, LAT are the associated station's geodetic latitude and
    longitude.  Note that the frame definitions below actually
    provide Euler angles for the inverse of M and use units of
    degrees, so the angle sequences are
 
       -1                         o          o
      M   =  [ -LON ]   [ LAT - 90 ]    [ 180 ]
                     3               2         3
 
          =  [ -(-111.92848132), (33.4179609 - 90), 180.0]
 
          =  [111.92848132, -56.5820391, 180.0]
 
 
begindata
    SITES = ('ASU-GS', 'LA-00', 'CH-00', 'HO-00', 'BA-00', 'AT-00', 'MI-00')
 
    ASU-GS_CENTER   = 399
    ASU-GS_FRAME    = 'IAU_EARTH'
    ASU-GS_IDCODE   = -9999999
    ASU-GS_LATLON   = (33.4179609, -111.92848132, .40)
    ASU-GS_UP       = 'Z'
    ASU-GS_NORTH    = 'X'
 
    FRAME_ASU-GS_TOPO               = -8999999
    FRAME_-8999999_NAME              = 'ASU-GS_TOPO'
    FRAME_-8999999_CLASS             = 4
    FRAME_-8999999_CLASS_ID          = -8999999
    FRAME_-8999999_CENTER            = -9999999
 
    OBJECT_-9999999_FRAME             = 'ASU-GS_TOPO'
 
    TKFRAME_ASU-GS_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_ASU-GS_TOPO_SPEC        = 'ANGLES'
    TKFRAME_ASU-GS_TOPO_UNITS       = 'DEGREES'
    TKFRAME_ASU-GS_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_ASU-GS_TOPO_ANGLES      = (111.92848132, -56.5820391, 180.0)
 
 LA-00_CENTER   = 399
    LA-00_FRAME    = 'IAU_EARTH'
    LA-00_IDCODE   = -1111111
    LA-00_LATLON   = (34.0522, -118.2437, .071)
    LA-00_UP       = 'Z'
    LA-00_NORTH    = 'X'
 
    FRAME_LA-00_TOPO               = -2111111
    FRAME_-2111111_NAME              = 'LA-00_TOPO'
    FRAME_-2111111_CLASS             = 4
    FRAME_-2111111_CLASS_ID          = -2111111
    FRAME_-2111111_CENTER            = -1111111
 
    OBJECT_-1111111_FRAME             = 'LA-00_TOPO'
 
    TKFRAME_LA-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_LA-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_LA-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_LA-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_LA-00_TOPO_ANGLES      = (118.2437, -55.9478, 180.0)
 
CH-00_CENTER   = 399
    CH-00_FRAME    = 'IAU_EARTH'
    CH-00_IDCODE   = -2222222
    CH-00_LATLON   = (41.8781, -87.6298, .181)
    CH-00_UP       = 'Z'
    CH-00_NORTH    = 'X'
 
    FRAME_CH-00_TOPO               = -3222222
    FRAME_-3222222_NAME              = 'CH-00_TOPO'
    FRAME_-3222222_CLASS             = 4
    FRAME_-3222222_CLASS_ID          = -3222222
    FRAME_-3222222_CENTER            = -2222222
 
    OBJECT_-2222222_FRAME             = 'CH-00_TOPO'
 
    TKFRAME_CH-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_CH-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_CH-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_CH-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_CH-00_TOPO_ANGLES      = (87.6298, -48.1219, 180.0)
 
HO-00_CENTER   = 399
    HO-00_FRAME    = 'IAU_EARTH'
    HO-00_IDCODE   = -3333333
    HO-00_LATLON   = (29.7604, -95.3698, .024)
    HO-00_UP       = 'Z'
    HO-00_NORTH    = 'X'
 
    FRAME_HO-00_TOPO               = -4333333
    FRAME_-4333333_NAME              = 'HO-00_TOPO'
    FRAME_-4333333_CLASS             = 4
    FRAME_-4333333_CLASS_ID          = -4333333
    FRAME_-4333333_CENTER            = -333333
 
    OBJECT_-3333333_FRAME             = 'HO-00_TOPO'
 
    TKFRAME_HO-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_HO-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_HO-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_HO-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_HO-00_TOPO_ANGLES      = (95.3698, -60.2396, 180.0)
 
BA-00_CENTER   = 399
    BA-00_FRAME    = 'IAU_EARTH'
    BA-00_IDCODE   = -4444444
    BA-00_LATLON   = (39.2904, -76.6122, .146)
    BA-00_UP       = 'Z'
    BA-00_NORTH    = 'X'
 
    FRAME_BA-00_TOPO               = -5444444
    FRAME_-5444444_NAME              = 'BA-00_TOPO'
    FRAME_-5444444_CLASS             = 4
    FRAME_-5444444_CLASS_ID          = -5444444
    FRAME_-5444444_CENTER            = -4444444
 
    OBJECT_-4444444_FRAME             = 'BA-00_TOPO'
 
    TKFRAME_BA-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_BA-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_BA-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_BA-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_BA-00_TOPO_ANGLES      = (76.6122, -50.7096, 180.0)
 
AT-00_CENTER   = 399
    AT-00_FRAME    = 'IAU_EARTH'
    AT-00_IDCODE   = -5555555
    AT-00_LATLON   = (33.749, -84.388, .32)
    AT-00_UP       = 'Z'
    AT-00_NORTH    = 'X'
 
    FRAME_AT-00_TOPO               = -6555555
    FRAME_-6555555_NAME              = 'AT-00_TOPO'
    FRAME_-6555555_CLASS             = 4
    FRAME_-6555555_CLASS_ID          = -6555555
    FRAME_-6555555_CENTER            = -5555555
 
    OBJECT_-5555555_FRAME             = 'AT-00_TOPO'
 
    TKFRAME_AT-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_AT-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_AT-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_AT-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_AT-00_TOPO_ANGLES      = (84.388, -56.251, 180.0)
 
MI-00_CENTER   = 399
    MI-00_FRAME    = 'IAU_EARTH'
    MI-00_IDCODE   = -6666666
    MI-00_LATLON   = (44.9778, -93.2650, .253)
    MI-00_UP       = 'Z'
    MI-00_NORTH    = 'X'
 
    FRAME_MI-00_TOPO               = -7666666
    FRAME_-7666666_NAME              = 'MI-00_TOPO'
    FRAME_-7666666_CLASS             = 4
    FRAME_-7666666_CLASS_ID          = -7666666
    FRAME_-7666666_CENTER            = -6666666
 
    OBJECT_-6666666_FRAME             = 'MI-00_TOPO'
 
    TKFRAME_MI-00_TOPO_RELATIVE    = 'IAU_EARTH'
    TKFRAME_MI-00_TOPO_SPEC        = 'ANGLES'
    TKFRAME_MI-00_TOPO_UNITS       = 'DEGREES'
    TKFRAME_MI-00_TOPO_AXES        = ( 3, 2, 3)
    TKFRAME_MI-00_TOPO_ANGLES      = (93.2650, -45.0222, 180.0)
 
 
 
 
 
begintext
 
[End of definitions file]
 
