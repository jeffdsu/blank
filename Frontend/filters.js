blankApp.filter('authorFilter', function () {
    return function (author) {
        if (author) {
            temp_str = "<a href='#/inspiration-corner/authors/" + author.id + "'>" + author.first_name + " ";
            if (author.middle_initial) {
                temp_str += author.middle_initial + " "
            }
            temp_str += author.last_name + "</a>";
            return temp_str;
        }
    };
});


blankApp.filter('insightColorFilter', function () {
    return function (insight, keywords) {
        if (insight && keywords) {
            temp_arr = insight.lesson.split(" ");
            temp_str = "";
            for (i = 0; i < temp_arr.length; i++) {
                var myRegexp = /(\w+)/g;
                var match = myRegexp.exec(temp_arr[i]);
                if (match && match[1] in keywords) {
                    var res = temp_arr[i].replace(match[1], '<span class="impacted_word_' + keywords[match[1]][0] + '">' + match[1] + '</span>');
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