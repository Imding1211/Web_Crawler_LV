document.addEventListener('DOMContentLoaded', function () {
    fetch('data.json')
        .then(response => response.json())
        .then(data => generateTable(data))
        .catch(error => console.error('Error loading JSON:', error));

    function generateTable(data) {
        const tableContainer = document.getElementById('table-container');

        const table = document.createElement('table');

        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        const headers = ['ID', 'Images', 'Region', 'Name', 'Price', 'URL'];
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');

        Object.keys(data).forEach(id => {
            const { img_num, product_info } = data[id];
            const regions = Object.keys(product_info);
            regions.forEach((region, index) => {
                const item = product_info[region];
                const row = document.createElement('tr');

                if (index === 0) {
                    const idCell = document.createElement('td');
                    idCell.rowSpan = regions.length;
                    idCell.textContent = id;
                    row.appendChild(idCell);

                    const imagesCell = document.createElement('td');
                    imagesCell.rowSpan = regions.length;
                    for (let i = 1; i <= img_num; i++) {  // 假設最多3張圖片
                        const img = document.createElement('img');
                        img.src = `image/side_trunk/${id}/${id}-${i}.png`;
                        img.alt = `${item.Name} Image ${i}`;
                        img.style.width = '100px'; // 可以根據需要調整圖片大小
                        imagesCell.appendChild(img);
                    }
                    row.appendChild(imagesCell);
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
