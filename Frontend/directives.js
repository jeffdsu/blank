blankApp.directive('styledInsight', ['insightService', function(insightService) {
  return {
    templateUrl: 'partials/styled-insight.htm',
    scope: {
        book: '='
    },
    
  };
}]);

blankApp.directive('styledKeywords', ['insightService', function(insightService) {
  return {
    templateUrl: 'partials/styled-keywords.htm',
    scope: {
        book: '='
    },
    
  };
}]);


blankApp.directive('styledInsightsList', ['insightService', function(insightService) {
  return {
    templateUrl: 'partials/styled-insights-list.htm',
    scope: {
        insightsList: '=',
        linkType: '@',
        medium:'='
    },
    
  };
}]);
