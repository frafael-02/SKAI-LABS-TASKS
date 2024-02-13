import './style.css';
import {Feature, Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import polygonJSON from './polygon'
import VectorSource from "ol/source/Vector";
import {Polygon} from "ol/geom";
import VectorLayer from "ol/layer/Vector";


//create a new feature with the coordinates and the type
const feature = new Feature({
  type: 'Polygon',
  geometry: new Polygon([polygonJSON.polygon]).transform('EPSG:4326','EPSG:3857'),
  name: 'Polygon',
});

//create a new layer with the source that contains the feature
let polygon = new VectorLayer({
  source: new VectorSource({
    features: [feature]
  }),
});

//create the map to display the layer
const map = new Map({
  target: 'map',
  layers: [
      new TileLayer({
        source:new OSM()
      }),
      polygon
  ],
  view: new View({
    center: [0, 0],
    zoom: 2
  })
});

//center the map on the polygon and add some padding so whole polygon is clearly visible
map.getView().fit(feature.getGeometry(), {padding: [20,20,20,20]});


