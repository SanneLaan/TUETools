/**
 * Created by Dion on 6-1-2017.
 */

var CoursesListPage = {
	init: function() {
		this.$container = $('.courses-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-ok', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

var DocumentsListPage = {
	init: function() {
		this.$container = $('.documents-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-ok', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

$(document).ready(function() {
	CoursesListPage.init();
	DocumentsListPage.init();
});