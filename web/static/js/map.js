window.onload = function() {
    var areas = document.querySelectorAll('area');
    
    areas.forEach(function(area) {
        area.addEventListener('mouseover', function() {
            this.classList.add('highlight');
        });
        
        area.addEventListener('mouseout', function() {
            this.classList.remove('highlight');
        });

        area.addEventListener('click', function() {
            this.classList.toggle('highlight');
        });
    });
};