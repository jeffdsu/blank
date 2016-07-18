blankApp.directive('styledInsight', ['insightService', function(insightService) {
  return {
    templateUrl: 'partials/styled-insight.htm',
    scope: {
        medium: '='
    },
    
  };
}]);

blankApp.directive('styledKeywords', ['insightService', function(insightService) {
  return {
    templateUrl: 'partials/styled-keywords.htm',
    scope: {
        medium: '='
    },
    
  };
}]);


blankApp.directive('styledInsightsList', ['insightService', 'Auth', function(insightService, Auth) {
  return {
    templateUrl: 'partials/styled-insights-list.htm',
    scope: {
        insightsList: '=',
        linkType: '@',
        medium:'=',
        home: '='
    },
    
  };
}]);


blankApp.directive('attachToInsight', ['insightService', 'Auth', function(insightService, Auth) {
  return {
    templateUrl: 'partials/attach-to-insight.htm',
    scope: {
        insight: '=',
        show: '@'
    },
    
  };
}]);

blankApp.directive('attachAMoment', ['insightService', 'Auth', function(insightService, Auth) {
  return {
    templateUrl: 'partials/attach-a-moment.htm',
    scope: {
        show: '@',
        insight: '='
    },
    
  };
}]);

blankApp.directive('attachAMedium', ['insightService', 'Auth', function(insightService, Auth) {
  return {
    templateUrl: 'partials/attach-a-medium.htm',
    scope: {
        show: '@',
        insight: '='
    },
    
  };
}]);


blankApp.directive('addToAList', ['insightService', 'Auth', function(insightService, Auth) {
  return {
    templateUrl: 'partials/add-to-a-list.htm',
    scope: {
        title: '@',
        listOfStuff: '='
    },
    
  };
}]);


blankApp.directive('addMedium', ['mediaService', 'Auth', function(mediaService, Auth) {
  return {
    templateUrl: 'partials/add-medium.htm',
    scope: {
        medium:'=',
        insight: '='
    },
    
  };
}]);