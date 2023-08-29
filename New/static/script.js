document.addEventListener("DOMContentLoaded", function () {
    var predictForm = document.getElementById("prediction-form");
    var viewReportButton = document.getElementById("view-report-button");

    if (predictForm && viewReportButton) {
        predictForm.addEventListener("submit", function (event) {
            event.preventDefault();

            // Get values from input fields
            var formData = new FormData(predictForm);
            var url = "/generate_pdf";

            // Send POST request with form data
            fetch(url, {
                method: "POST",
                body: formData
            })
            .then(response => response.blob())  // Changed to blob() to handle PDF response
            .then(data => {
                // Create a blob URL for the PDF and open it in a new tab
                var pdfBlob = new Blob([data], { type: "application/pdf" });
                var pdfUrl = URL.createObjectURL(pdfBlob);
                window.open(pdfUrl, "_blank");
            })
            .catch(error => {
                console.error("An error occurred:", error);
            });
        });

        viewReportButton.addEventListener("click", function () {
            // Redirect to the report page
            window.location.href = "/report";
        });
    }
});