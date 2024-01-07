
// const title = document.getElementById("title");
// const body = document.getElementById("body");
// const gender = document.getElementById("gender");
// const reportDate = document.getElementById("reportDate");

// document.getElementById("addReportForm").addEventListener("submit", e => {
//     e.preventDefault();
    
//     let newData = {
//         title: title.value,
//         body: body.value,
//         date: reportDate.value,
//     }

//     const storedDataJSON = localStorage.getItem('reports');
//     if (storedDataJSON !== null) {
//         // The item exists in localStorage
//         let tableData = JSON.parse(storedDataJSON);
//         tableData.push(newData);
//         localStorage.setItem("reports", JSON.stringify(tableData));
//         getData();

//         // Clear fields
//         title.value = "";
//         body.value = "";
//         reportDate.value = "";
//     }
// });
