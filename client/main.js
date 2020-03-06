var themeSwitch = document.getElementById("themeSwitch");
var root = document.documentElement;
  themeSwitch.addEventListener("change", function(event) {
    resetTheme(); // update color theme
  });

  function resetTheme() {
    if (themeSwitch.checked) {
        root.style.setProperty('--primary-color', '#121212')
        root.style.setProperty('--terciary-color', '#f5f5f5')
        root.style.setProperty('--card-color', '#383838')
        root.style.setProperty('--card-text', '#f5f5f5')
        root.style.setProperty('--card-border', '1px solid #95d47fb4')
    }else{
        root.style.setProperty('--primary-color', '#f5f5f5')
        root.style.setProperty('--terciary-color', '#020024')
        root.style.setProperty('--card-color', '#ffffff')
        root.style.setProperty('--card-text', '#383838')
        root.style.setProperty('--card-border', '1px solid #e9e9e9f6')
    }
  }

var modal_close = document.getElementById("modal_close");
var modal_open = document.getElementById("modal_open");
var modal = document.getElementById("cfg_modal");

modal_close.addEventListener("click", function(){
  modal.classList.add("hidden");
});

modal_open.addEventListener("click", function(){
  modal.classList.remove("hidden");
});

