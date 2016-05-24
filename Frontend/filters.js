blankApp.filter('contributionFilter', function () {
    return function (contribution) {
        if (contribution) {
            temp_str = "<h4><a class=\"contributor\"/href='#/inspiration-corner/contributors/" + contribution.contributor.id + "'>" + contribution.contributor.first_name + " ";
            if (contribution.contributor.middle_initial) {
                temp_str += contribution.contributor.middle_initial + " "
            }
            temp_str += contribution.contributor.last_name + "</a><h4>";
            return temp_str;
        }
    };
});

blankApp.filter('addUserLinkFilter', function(){
    return function (input_str, obj) {
         input_str = "<a href=\"#inspiration-corner/users/" + obj.user + "\" class=\"insight\">" + input_str + "</a>";
        return input_str;
    };             
});

blankApp.filter('addMediumLinkFilter', function(){
    return function (input_str, obj) {
         input_str = "<a href=\"#inspiration-corner/media/" + obj.related_medium_type + "/" + obj.medium + "\" class=\"insight\">" + input_str + "</a>";
        return input_str;
    };             
});


blankApp.filter('insightColorFilter', function () {
    return function (insight, list_of_keywords) {
        if (insight && list_of_keywords) {
        
            var keywords = {};
//            Jeff - I need helpd with this syntax
            for (var i=0; i < list_of_keywords.length; i++){
                keywords [list_of_keywords[i].word] = list_of_keywords[i];
            }
            
            
            temp_arr = insight.lesson.split(" ");
            temp_str = "";
            
            for (i = 0; i < temp_arr.length; i++) {
                var myRegexp = /(\w+)/i;
                var match = myRegexp.exec(temp_arr[i]);
                if (match && match[1].toLowerCase() in keywords) {
                   
                    var res = temp_arr[i].replace(match[1], '<span class="impacted_word_' + i + '">' + match[1] + '</span>');
                    temp_str += res + " ";
                } else {
                    temp_str += temp_arr[i] + " ";
                }
            }
            return temp_str;
        }
        return "";
    };
});


blankApp.filter('insightLinkToUserFilter', function () {
    return function (insight) {
        if (insight) {
            return "<a href='#/inspiration-corner/users/" + insight.user + "'>" + insight.lesson + "</a>";
        }
        return "";
    };
});


blankApp.filter('keywordsFilter', function () {
    return function (items, search) {
        var filtered = [];
        if (search) {
            search_words = search.split(" ");

            angular.forEach(search_words, function (word) {
                angular.forEach(items, function (item) {
                    if (word.toLowerCase() in item.keywords) {
                        filtered.push(item);
                    }
                });
            });
            return filtered;
        }
        return items;

    };
});