blankApp.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {

    $routeProvider

        .when('/inspiration-corner', {
            templateUrl: 'partials/inspiration.htm'
            , controller: 'inspirationController'
        })
        .when('/inspiration-corner/media/:mediaType', {
            templateUrl: 'partials/books.htm'
            , controller: 'mediaController'
        })
        .when('/inspiration-corner/media/:mediaType/:mediaId', {
            templateUrl: 'partials/book-details.htm'
            , controller: 'mediaDetailController'
        })
        .when('/signin', {
            templateUrl: 'partials/signin.htm'
            , controller: 'authController'
        })
        .when('/signout', {
            templateUrl: 'partials/signout.htm'
            , controller: 'authController'
        })
        .when('/signup', {
            templateUrl: 'partials/signup.htm'
            , controller: 'authController'
        })
        .when('/inspiration-corner/authors', {
            templateUrl: 'partials/authors.htm'
            , controller: 'authorsController'
        })
        .when('/inspiration-corner/authors/:authorId', {
            templateUrl: 'partials/author-details.htm'
            , controller: 'authorDetailsController'
        })
        .when('/inspiration-corner/users/:userId', {
            templateUrl: 'partials/user-details.htm'
            , controller: 'userDetailsController'
        })
        // admin
        .when('/inspiration-corner/admin', {
            templateUrl: 'partials/admin.htm'
            , 
        })
        .when('/inspiration-corner/admin/mediums/books/add', {
            templateUrl: 'partials/admin/mediums/books/add-book.htm'
            , controller: 'adminBooksController'
        })
        .when('/inspiration-corner/admin/authors/add', {
            templateUrl: 'partials/admin-add-author.htm'
            , controller: 'adminAuthorController'
        })
        .when('/inspiration-corner/admin/mediums/books', {
            templateUrl: 'partials/admin/mediums/books/add-book.htm'
            , controller: 'adminBooksController'
        })
        .when('/inspiration-corner/admin/words-to-ignore', {
            templateUrl: 'partials/admin-words-to-ignore.htm'
            , controller: 'adminWordsToIgnoreController'
        })
        .when('/inspiration-corner/admin/insights', {
            templateUrl: 'partials/admin-insights.htm'
            , controller: 'adminInsightController'
        });

}]);