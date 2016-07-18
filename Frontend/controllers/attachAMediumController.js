blankApp.controller('attachAMediumController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'mediaService', 'mediumTypeService', 'insightService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, mediaService, mediumTypeService, insightService) {

    $scope.new = false;
    $scope.medium = mediaService.new_medium;
    
    $scope.set_new = function () {
        $scope.new = !$scope.new;
    };

    
    mediumTypeService.get_collection()
    .then(function(medium_types){
        $scope.medium_types = medium_types;
        
    }, function(err) {
        
    });
    
    $scope.get_media = function(medium_type) {
        console.log(medium_type);
        mediaService.get_collection(medium_type)
        .then(function(media){
            $scope.media = media;
        }, function(err) {});
        
    };
    
    
    $scope.attach_medium = function(insight, medium) {
        
        insight.medium = medium;
        
        insightService.update(insight).then(function(
                                            
        ){}, function(err){})
        
    };
    
    
    
    

    

}]);