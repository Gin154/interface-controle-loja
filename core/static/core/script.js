document.addEventListener('DOMContentLoaded', function () {
    const cpfInput = document.getElementById('caixacpf');
    cpfInput.addEventListener('input', function (e) {
        let value = e.target.value.replace(/\D/g, ''); // Remove non-digit characters
        value = value.replace(/^(\d{3})(\d)/, '$1.$2'); // Add first dot
        value = value.replace(/(\d{3})(\d)/, '$1.$2'); // Add second dot
        value = value.replace(/(\d{3})(\d{2})$/, '$1-$2'); // Add dash
        e.target.value = value;
    });
});