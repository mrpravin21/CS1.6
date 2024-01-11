/* JavaScript to Change Background Color */
document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    form.addEventListener('mouseover', function () {
      document.body.style.backgroundColor = 'white'; 
    });
    form.addEventListener('mouseout', function () {
      document.body.style.backgroundColor = 'lightblue'; 
    });
  });
  