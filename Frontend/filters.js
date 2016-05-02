blankApp.filter('authorFilter', function() {
  return function(author) {
   return author.first_name + " " + author.last_name;
  };
});


blankApp.filter('insightFilter', function() {
  return function(insight) {
    return author.first_name + " " + author.last_name;
  };
});