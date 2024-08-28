
i18next
    .use(i18nextHttpBackend)
    .use(i18nextBrowserLanguageDetector)
    .init({
        fallbackLng: 'mr', // Default language
        debug: true,
        backend: {
            loadPath: '/locales/{{lng}}/{{ns}}.json' // Path to your JSON files
        }
    }, function (err, t) {
        if (err) return console.error(err);
        updateContent(); // Function to update content after language change
    });

function updateContent() {
    document.querySelectorAll('[data-i18n]').forEach(function (element) {
        const key = element.getAttribute('data-i18n');
        element.innerHTML = i18next.t(key); // Update innerHTML with translated text
    });
}

function changeLanguage(lng) {
    i18next.changeLanguage(lng, function (err, t) {
        if (err) return console.error(err);
        updateContent(); // Update content when language changes
    });
}
