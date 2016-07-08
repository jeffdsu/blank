blankApp.filter('contributionFilter', function () {
    return function (contribution) {
        if (contribution) {
            temp_str = "<span><h4><a class=\"contributor\"/href='#/inspiration-corner/contributors/" + contribution.contributor.id + "'>" + contribution.contributor.first_name + " ";
            if (contribution.contributor.middle_initial) {
                temp_str += contribution.contributor.middle_initial + " "
            }
            temp_str += contribution.contributor.last_name + "</a></h4></span>";
            //temp_str += "<span><i>" + contribution.type.name + "<i></span>"
            return temp_str;
        }
    };
});


blankApp.filter('addLinkFilter', function () {
    return function (input_str, obj, type) {
        console.log(type);
        if (type === 'medium') {
            input_str = "<a href=\"#inspiration-corner/media/" + obj.related_medium_type + "/" + obj.medium + "\" class=\"insight\">" + input_str + "</a>";
            return input_str;
        } else if (type === 'user') {
            input_str = "<a href=\"#inspiration-corner/users/" + obj.user.id + "\" class=\"insight\">" + input_str + "</a>";
            return input_str;
        }

    };
});




blankApp.filter('insightColorFilter', function () {
    return function (insight, list_of_keywords) {
        if (insight && list_of_keywords) {

            var keywords = {};
            //            Jeff - I need helpd with this syntax
            for (var i = 0; i < list_of_keywords.length; i++) {
                keywords[list_of_keywords[i].word] = [i, list_of_keywords[i]];
            }


            temp_arr = insight.lesson.split(" ");
            temp_str = "";

            for (i = 0; i < temp_arr.length; i++) {
                var myRegexp = /(\w+)/i;
                var match = myRegexp.exec(temp_arr[i]);
                if (match && match[1].toLowerCase() in keywords) {

                    var res = temp_arr[i].replace(match[1], '<span class="impacted_word_' + keywords[match[1].toLowerCase()][0] + '">' + match[1] + '</span>');
                    temp_str += res + " ";
                } else {
                    temp_str += temp_arr[i] + " ";
                }
            }
            return temp_str;
        }
        else if (insight){
            if (insight.valid === false) {
                return '<div class="invalid">' + insight.lesson + '</div>';
            }
            return insight.lesson;
        }
        return "";
    };
});


blankApp.filter('insightLinkToUserFilter', function () {
    return function (insight) {
        if (insight) {
            return "<a href='#/inspiration-corner/users/" + insight.user + "'>" + insight.lesson + "</a><i>";
        }
        return "";
    };
});

blankApp.filter('stuffFilter', function () {
    return function (stuff) {
        var str="";
        
        
        for (var attr in stuff) {
           
           if (attr === 'type') {
                str+="<td>";
               str+=stuff[attr].name;
               str+="</td>";
               
           }
           else if (attr === 'contributor') {
               str+="<td>";
               str+=stuff[attr].first_name + " " +  stuff[attr].last_name;
               str+="</td>";
           }
            else if (attr === 'link') {
                str+="<td>";
               str+=stuff[attr];
                str+="</td>";
           }
           
            
        }
        console.log(str);
        return str;
    };
});




blankApp.filter('insightsFilter', function () {
    return function (items, search, tag_filter) {

        
        if (tag_filter) {
            var temp_array = []
            angular.forEach(items, function (item) {
                angular.forEach(item.tags, function (tag) {
                    console.log(tag.tag);
                    if (tag_filter.id == tag.tag.id) {
                        temp_array.push(item);
                    }
                });    
            });
            items = temp_array;
        }

        var filtered = [];
        if (search) {

            search_words = search.split(" ");
            angular.forEach(search_words, function (word) {
                angular.forEach(items, function (item) {
                    var re = new RegExp(word, "i");
                    if (item.lesson.search(re)>=0) {

                        filtered.push(item);
                    }
                });
            });
            return filtered;
        }
        return items;

    };
});

blankApp.filter('keywordsFilter', function () {
    return function (items, search) {
        console.log(search);
        var filtered = [];
        if (search) {
            search_words = search.split(" ");

            
            angular.forEach(search_words, function (word) {
                angular.forEach(items, function (item) {
                    var keywords = {};
                        //            Jeff - I need helpd with this syntax
                        for (var i = 0; i < item.top_10_keywords.length; i++) {
                            keywords[item.top_10_keywords[i].word] = [i, item.top_10_keywords[i]];
                        }
                    if (word.toLowerCase() in keywords) {
                        
            
                        filtered.push(item);
                    }
                });
            });
            return filtered;
        }
        return items;

    };
});