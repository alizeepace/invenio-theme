# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Test for theme module."""

from __future__ import absolute_import, print_function

from flask import Blueprint, abort


def test_page_error_handler_401(app_error_handler):
    """Testing error handler with 401 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 401 error.
    @blueprint.route('/error_401')
    def error_401():
        return abort(401)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_401')
        assert response.status_code == 401
        assert b'<h1><i class=\"fa fa-flash\"></i>' in response.data
        assert b'Unauthorized</h1>' in response.data
        assert b'<p>You need to be authenticated' in response.data
        assert b'to view this page.</p>' in response.data


def test_page_error_handler_403(app_error_handler):
    """Testing error handler with 403 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 403 error.
    @blueprint.route('/error_403')
    def error_403():
        return abort(403)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_403')
        assert response.status_code == 403
        assert b'<h1><i class="fa fa-flash"></i>' in response.data
        assert b'Permission required</h1>' in response.data
        assert b'<p>You do not have sufficient permissions' in response.data
        assert b'to view this page.</p>' in response.data


def test_page_error_handler_404(app_error_handler):
    """Testing error handler with 404 error code."""
    with app_error_handler.test_client() as client:
        response = client.get('/ThisPathDoesNotExists')
        assert response.status_code == 404
        assert b'<h1><i class="fa fa-flash"></i>' in response.data
        assert b'Page not found</h1>' in response.data
        assert b'<p>The page you are looking for' in response.data
        assert b'could not be found.</p>' in response.data


def test_page_error_handler_500(app_error_handler):
    """Testing error handler with 401 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 401 error.
    @blueprint.route('/error_500')
    def error_500():
        return abort(500)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_500')
        assert response.status_code == 500
        assert b'<h1><i class=\"fa fa-flash\"></i>' in response.data
        assert b'Internal server error</h1>' in response.data
