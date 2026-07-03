document.addEventListener("DOMContentLoaded", function () {
    const htmlElement = document.documentElement;
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");
    const themeLabel = document.getElementById("theme-label");

    const savedTheme = localStorage.getItem("sportsAppTheme");

    if (savedTheme === "dark" || savedTheme === "light") {
        htmlElement.setAttribute("data-theme", savedTheme);
    } else {
        htmlElement.setAttribute("data-theme", "light");
    }

    updateThemeButton();

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const currentTheme = htmlElement.getAttribute("data-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";

            htmlElement.setAttribute("data-theme", newTheme);
            localStorage.setItem("sportsAppTheme", newTheme);

            updateThemeButton();
        });
    }

    function updateThemeButton() {
        const currentTheme = htmlElement.getAttribute("data-theme");

        if (!themeIcon || !themeLabel) {
            return;
        }

        if (currentTheme === "dark") {
            themeIcon.textContent = "☀️";
            themeLabel.textContent = "Light Mode";
        } else {
            themeIcon.textContent = "🌙";
            themeLabel.textContent = "Dark Mode";
        }
    }
});