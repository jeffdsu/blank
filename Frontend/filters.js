blankApp.filter('authorFilter', function() {
  return function(author) {
   return author.first_name + " " + author.last_name;
  };
});


blankApp.filter('insightFilter', function() {
  return function(insight, keywords) {
    if (insight && keywords){
        temp_arr = insight.lesson.split(" ");
        temp_str = "";
        for (i = 0; i < temp_arr.length; i++) {
            if (temp_arr[i] in keywords) {
                temp_str += '<b>' + temp_arr[i] + '</b>' + " ";
            }
            else {
                temp_str += temp_arr[i] + " ";
            }
        }
        return temp_str;
    }
    return "";
  };
});