function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    uploadInput = document.getElementById('fileInput');
    uploadBtn = document.getElementById('uploadBtn');
    load_file = document.querySelector('.load_file');
    load_file.style.display = 'none';
    loading = document.querySelector('.loading');
    loading.style.display = 'flex';
    uploadInput.style.display = 'none';
    uploadBtn.style.display = 'none';
    fetch('/upload/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loading.style.display = 'none';
        html = `<div class='info_file'>File ${data.filename} uploaded (${data.size} bytes)</div>
                <div class="table_response">`;
        data.report.forEach(site => {
            html += `<div class='site'>
                <div class='site_title'>${site.site_name}</div>`;
            if (site.check_error === false){
                html += `<div class='error_not'>Ошибок нет</div>`;
            } else{
                html += `<div class='error_yes'>Ошибки есть</div>`;
            }
            let i = 0;
            site.products_error.forEach(product =>{
                i = i+1;
                if (product.offer_error === false){
                    html += `<div class='product error_not'>`;
                } else {
                    html += `<div class='product error_yes'>`;
                }

                html += `<span class="product_number">${i}</span>
                    <span class="product_id">id:${product.offer_id}</span>
                    <span class="product_name">name:${product.offer_name}</span>`;
                html += `</div>`;
            })
            html += `</div>`;
        });
        html += `</div>`;
        document.getElementById('result').innerHTML = html;
    })
    .catch(error => console.error('Error:', error));
    uploadInput.style.display = 'flex';
    uploadBtn.style.display = 'flex';
}

function loadSites() {
    $.get("/sites/", function(data) {
        let html = '<table><tr><th>ID</th><th>Name</th><th>URL</th><th>Filename</th></tr>';
        data.forEach(site => {
            html += `<tr>
                <td class="site-id-${site.id}">${site.id}</td>
                <td class="site-name-${site.id}"><a href="/admin/site/${site.id}">${site.name}</a></td>
                <td class="site-url-${site.id}"><a href="${site.url}">${site.url}</a></td>
                <td class="site-file-${site.id}">${site.filename}</td>
                <td class="site-update-${site.id}"><button onclick='updateSiteBtn(${site.id});'>✏️</button></td>
                <td class="site-delete-${site.id}"><button onclick='deleteSite(${site.id});'>-</button></td>
            </tr>`;
        });
        html += `<tr>
            <td></td>
            <td><input class='new-site-name' name='new-site-name' placeholder="введите название сайта"></td>
            <td><input class='new-site-url' name='new-site-url' placeholder="введите ссылку сайта"></td>
            <td><input class='new-site-file' name='new-site-file' placeholder="введите название файла"></td>
            <td><button onclick='createSite();'>+</button></td></tr></table>`;
        $("#sites-list").html(html);
    });
}

function createSite() {
        const name = document.querySelector('.new-site-name').value;
        const url = document.querySelector('.new-site-url').value;
        const filename = document.querySelector('.new-site-file').value;
        arr = {name: name, url: url, filename: filename};
        const response = $.ajax({
                    url: '/sites/',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(arr),
                    success: function (response) {
                        if (response['status_code'] == 200){
                            console.log(response['detail']);
                            loadSites();
                        } else{
                            console.log(response['detail']);
                        }
                    },
                    error: function () {
                        console.log("error");
                    }
                });
    }

function updateSiteBtn(id) {
    const name = document.querySelector('.site-name-' + id).textContent;
    const url = document.querySelector('.site-url-' + id).textContent;
    const filename = document.querySelector('.site-file-' + id).textContent;
    document.querySelector('.site-name-' + id).innerHTML = `<input class='input-site-name-${id}' name='input-site-name' value='${name}'></input>`;
    document.querySelector('.site-url-' + id).innerHTML = `<input class='input-site-url-${id}' name='input-site-url' value='${url}'></input>`;
    document.querySelector('.site-file-' + id).innerHTML = `<input class='input-site-file-${id}' name='input-site-file' value='${filename}'></input>`;
    document.querySelector('.site-update-' + id).innerHTML = `<button onclick='updateSite(${id});'>✏️</button>`;
    document.querySelector('.site-delete-' + id).innerHTML = `<button onclick='cancelUpdateSiteBtn(${id});'>x</button>`;
}

function deleteSite(id) {
    const response = $.ajax({
                url: '/sites/' + id,
                type: 'DELETE',
                success: function (response) {
                    if (response['status_code'] == 200){
                        console.log(response['detail']);
                        loadSites();
                    } else{
                        console.log(response['detail']);
                    }
                },
                error: function () {
                    console.log("error");
                }
            });
}

function cancelUpdateSiteBtn(id) {
    document.querySelector('.site-name-' + id).innerHTML = '<a href="/admin/site/' + id + '">' + document.querySelector('.input-site-name-' + id).value + '</a>';
    document.querySelector('.site-url-' + id).innerHTML = '<a href="/admin/site/' + id + '">' + document.querySelector('.input-site-url-' + id).value + '</a>';
    document.querySelector('.site-file-' + id).innerHTML = document.querySelector('.input-site-file-' + id).value;
    document.querySelector('.site-update-' + id).innerHTML = `<button onclick='updateSiteBtn(${id});'>✏️</button>`;
    document.querySelector('.site-delete-' + id).innerHTML = `<button onclick='deleteSite(${id});'>-</button>`;
}

function updateSite(id) {
    const name = document.querySelector('.input-site-name-' + id).value;
    const url = document.querySelector('.input-site-url-' + id).value;
    const filename = document.querySelector('.input-site-file-' + id).value;
    arr = {name: name, url: url, filename: filename};
    const response = $.ajax({
                url: '/sites/' + id,
                type: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify(arr),
                success: function (response) {
                    if (response['status_code'] == 200){
                        console.log(response['detail']);
                        loadSites();
                    } else{
                        console.log(response['detail']);
                    }
                },
                error: function () {
                    console.log("error");
                }
            });
}

function createCategory(id) {
    const name = document.querySelector('.new-category-name').value;
    let parent_id = document.querySelector('.new-category-parent-id').value;
    const site_id = id;
    if (parent_id == '') {
        parent_id = null;
    }
    arr = {name: name, parent_id: parent_id, site_id: site_id};
    console.log(arr)
    const response = $.ajax({
                url: '/categories/',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(arr),
                success: function (response) {
                    if (response['status_code'] == 200){
                        console.log(response['detail']);
                        loadSites();
                    } else{
                        console.log(response['detail']);
                    }
                },
                error: function () {
                    console.log("error");
                }
            });
}

function updateCategoryBtn(id) {
    console.log(id);
    let name = document.querySelector('.category-name-' + id);
    console.log(name.textContext);
    let parent_id = document.querySelector('.category-parent-id-' + id).textContext;
    let product = document.querySelector('.category-product-' + id).textContent;
    const description = document.querySelector('.category-description-' + id).textContent;
//    document.querySelector('.category-name-' + id).innerHTML = `<input class='input-category-name-${id}' name='input-category-name' value='${name}'></input>`;
    document.querySelector('.category-parent-id-' + id).innerHTML = `<input class='input-category-parent-id-${id}' name='input-category-parent-id' value='${parent-id}'></input>`;
    document.querySelector('.category-product-' + id).innerHTML = `<input class='input-category-product-${id}' name='input-category-product' value='${product}'></input>`;
    document.querySelector('.category-description-' + id).innerHTML = `<input class='input-category-description-${id}' name='input-category-description' value='${description}'></input>`;
    document.querySelector('.category-update-' + id).innerHTML = `<button onclick='updateCategory(${id});'>✏️</button>`;
    document.querySelector('.category-delete-' + id).innerHTML = `<button onclick='cancelUpdateCategoryBtn(${id});'>x</button>`;
}

function cancelUpdateCategoryBtn(id) {
    document.querySelector('.category-name-' + id).innerHTML = document.querySelector('.input-category-name-' + id).value;
    document.querySelector('.category-parent-id-' + id).innerHTML = document.querySelector('.input-category-parent-id-' + id).value;
    document.querySelector('.category-product-' + id).innerHTML = document.querySelector('.input-category-product-' + id).value;
    document.querySelector('.category-description-' + id).innerHTML = document.querySelector('.input-category-description-' + id).value;
    document.querySelector('.category-update-' + id).innerHTML = `<button onclick='updateCategoryBtn(${id});'>✏️</button>`;
    document.querySelector('.category-delete-' + id).innerHTML = `<button onclick='deleteCategory(${id});'>-</button>`;
}

function updateCategory(id) {

}

function createProduct(id) {

}

function createDescription(id){

}