// from data.js
// function buildtable() {

  d3.json("/api/v1.0/Data", function (data) {

    console.log(data);
    var tableData = data
    // get table references
    var tbody = d3.select("tbody");
    function buildTable(data) {
      tbody.html("");
      Object.values(data).forEach((dataRow) => {
        // Append a row to the table bodys
        var row = tbody.append("tr");
        // Loop through each field in the dataRow and add
        Object.values(dataRow).forEach((val) => {
          var cell = row.append("td");
          cell.text(val);
        });
      });
    }
    var filters = {};
    function updateFilters() {
      // Save the element, value, and id of the filter that was changed
      var changedElement = d3.select(this).select("input");
      var elementValue = changedElement.property("value");
      var filterId = changedElement.attr("id");
      if (elementValue) {
        filters[filterId] = elementValue;
      }
      else {
        delete filters[filterId];
      }
      // Call function to apply all filters and rebuild the table
      // filterTable();
       // Set the filteredData to the tableData
       let filteredData = tableData;
       Object.entries(filters).forEach(([key, value]) => {
         filteredData = filteredData.filter(row => row[key] === value);
       });
       // Finally, rebuild the table using the filtered Data
       buildTable(filteredData);
    }
    
    d3.selectAll(".filter").on("change", updateFilters);
    // Build the table when the page loads
    buildTable(tableData);
  })