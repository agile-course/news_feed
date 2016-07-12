var app = angular.module('NewsFeed', ['ngResource', 'ui.bootstrap'])
.config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
.service('PostResource', ['$resource', function($resource) {
    this.Post = $resource("/post/:subreddit/:verb", {subreddit: '@subreddit'}, {
        'get': {
            method:'GET',
            params: {'verb': 'list'},
        },
        'create': {
            method:'POST',
            params: {'verb': 'create'},
        },
    });
}])
.service('SubredditResource', ['$resource', function($resource) {
    this.Subreddit = $resource("/subreddit/:verb", {}, {
        'get': {
            method:'GET',
            params: {'verb': 'list'},
        },
        'create': {
            method:'POST',
            params: {'verb': 'create'},
        },
    });
}])
.controller('HomepageController',
            ['$scope', '$timeout', 'filterFilter', 'PostResource', 'SubredditResource',
            function($scope, $timeout, filterFilter, PostResource, SubredditResource) {

    var currentSubreddit = 'global';
    self.getPosts = function() {
        return PostResource.Post.get({'subreddit': currentSubreddit}, function(result) {
            $scope.posts = result.posts;
        }).$promise;
    };
    $scope.refreshPosts = function(id) {
        currentSubreddit = id;
        self.getPosts();
    };

    // Initialize
    self.posts = [];
    getPosts().then(function() {
        $scope.createPost = function(title, content) {
            return PostResource.Post.create(
                {'subreddit': currentSubreddit, 'title': title, 'content': content},
                function(result) {
                // TODO | Highlight box red and alert user on error
                console.log(result);
                getPosts(); // Refresh visible posts
            }).$promise;
        };
    });



    var getSubreddits = function(){
        return SubredditResource.Subreddit.get(function(result) {
            $scope.subreddits = result.subreddits;
        }).$promise;
    };

    // Initialize
    $scope.subreddits = [];
    getSubreddits().then(function() {
        $scope.createSubreddit = function(title, description) {
            return SubredditResource.Subreddit.create(
                {'title': title, 'description': description},
                function(result) {
                    // TODO | Highlight box red and alert user on error
                    console.log(result);
                    getSubreddits(); // Refresh existing subreddits list
                });
        };
    });

}]);
