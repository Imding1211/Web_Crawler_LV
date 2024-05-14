document.addEventListener('DOMContentLoaded', function () {
    fetch('product_data.json')
        .then(response => response.json())
        .then(data => generateTable(data))
        .catch(error => console.error('Error loading JSON:', error));

    function generateTable(data) {
        const tableContainer = document.getElementById('table-container');

        const table = document.createElement('table');

        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        const headers = ['商品編號', '販售國家', '商品名稱', '商品價格', '商品連結'];
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');

        Object.keys(data).forEach(id => {
            const regions = Object.keys(data[id]);
            regions.forEach((region, index) => {
                const item = data[id][region];
                const row = document.createElement('tr');
                
                if (index === 0) {
                    const idCell = document.createElement('td');
                    idCell.rowSpan = regions.length;
                    idCell.textContent = id;
                    row.appendChild(idCell);
                }

                const regionCell = document.createElement('td');
                regionCell.textContent = region;
                row.appendChild(regionCell);

                const nameCell = document.createElement('td');
                nameCell.textContent = item.Name;
                row.appendChild(nameCell);

                const priceCell = document.createElement('td');
                priceCell.textContent = item.Price;
                row.appendChild(priceCell);

                const urlCell = document.createElement('td');
                const urlLink = document.createElement('a');
                urlLink.href = item.url;
                urlLink.target = "_blank";
                urlLink.textContent = "Link";
                urlCell.appendChild(urlLink);
                row.appendChild(urlCell);

                tbody.appendChild(row);
            });
        });

        table.appendChild(tbody);
        tableContainer.appendChild(table);
    }
});
