Oil spills in the Niger Delta associated with Shell Petroleum Development Company (of Nigeria) operations since January 2011. Data comes from Shell as listed on [their website](http://www.shell.com.ng/home/content/nga/environment_society/respecting_the_environment/oil_spills/monthly_data.html).

From the site: "SPDC has publicly reported oil spill statistics annually since 1995 and this website further enhances transparency by recording as fully as possible every spill that happens from our facilities as soon as it is possible to get accurate information. It tracks the progress of our spill response from when we learn about the leak to when clean-up is completed and signed off."

### Data

Unfortunately the data is loaded into each web page via javascript (this javascript is broken in major browsers (e.g. Chrome) and page shows as empty -- but does work in Firefox) but a bit of digging revealed source xml files, which are of the form:

http://www.shell.com.ng/home/page/nga/environment_society/respecting_the_environment/oil_spills/data_{month}.xml

For example: http://www.shell.com.ng/home/page/nga/environment_society/respecting_the_environment/oil_spills/data_january.xml

Main google docs spreadsheet contains full scrape of data scripted by Mikel Maron while second sheet represents the an initial extract and geocode by hand.

The additional "environmental incidents" CSV attached to this page is drawn from the Ushahidi instance at http://nigerdeltawatch.org/ and contains 75 environmental incidents extracted from http://www.nigerdeltawatch.org/api/?task=incidents&by=catid&id=14 and converted to GeoJSON using https://gist.github.com/1420102 and then converted to CSV as described on that gist.

### Visualizations

Visualizations are just for November 2011 data and are designed as proof of concept.

* Fusion tables map: https://www.google.com/fusiontables/DataSource?snapid=S329812EPDw
* [TileMill map](http://a.tiles.mapbox.com/v3/ericg.map-h8cnijfc.html#7.00/6.582/7.458)

### License

* Assume Shell is asserting no exclusive rights in the data (though no explicit license). Maintainer is licensing under the PDDL

