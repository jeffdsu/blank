blankApp.filter('authorFilter', function() {
  return function(author) {
   return "<a href='#/inspiration/authors/" + author.id + "'>" + author.first_name + " " + author.last_name + "</a>";
  };
});


blankApp.filter('insightColorFilter', function() {
  return function(insight, keywords) {
    if (insight && keywords){
        temp_arr = insight.lesson.split(" ");
        temp_str = "";
        for (i = 0; i < temp_arr.length; i++) {
            if (temp_arr[i] in keywords) {
                temp_str += '<span class="impacted_word_' + keywords[temp_arr[i]][0] +  '">' + temp_arr[i] + '</span>' + " ";
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


blankApp.filter('insightLinkToUserFilter', function() {
  return function(insight) {
      if (insight) {
          return "<a href='#/inspiration/users/" + insight.user + "'>" + insight.lesson + "</a>";
      }
      return "";
  };
});