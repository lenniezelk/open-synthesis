"""Analysis of Competing Hypotheses Django Application URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

# NOTE: Django's API doesn't follow constant naming convention for 'app_name' and 'urlpatterns'

app_name = 'openach'  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^$', views.site.index, name='index'),
    # NOTE: when running the dev server, Django will try to serve from the static file provider b/c of static prefix
    url(r'^static/images/bitcoin\.svg$', views.site.bitcoin_qrcode, name='bitcoin_donate'),
    url(r'^boards/$', views.boards.board_listing, name='boards'),
    url(r'^accounts/(?P<account_id>[0-9]+)/boards/', views.boards.user_board_listing, name='user_boards'),
    url(r'^accounts/notifications/clear', views.notifications.clear_notifications, name='clear_notifications'),
    url(r'^accounts/notifications/', views.notifications.notifications, name='notifications'),

    url(r'^teams/create$', views.teams.create_team, name='create_team'),
    url(r'^teams/$', views.teams.team_listing, name='teams'),
    url(r'^teams/(?P<team_id>[0-9]+)/join/$', views.teams.join_team, name='join_team'),
    url(r'^teams/(?P<team_id>[0-9]+)/leave/$', views.teams.leave_team, name='leave_team'),
    url(r'^teams/(?P<team_id>[0-9]+)/$', views.teams.view_team, name='view_team'),
    url(r'^teams/(?P<team_id>[0-9]+)/edit/$', views.teams.edit_team, name='edit_team'),
    url(r'^teams/(?P<team_id>[0-9]+)/members/$', views.teams.team_members, name='team_members'),
    url(r'^teams/(?P<team_id>[0-9]+)/members/invite/$', views.teams.invite_members, name='invite_members'),
    url(r'^teams/(?P<team_id>[0-9]+)/members/(?P<member_id>[0-9]+)/revoke/$', views.teams.revoke_membership, name='revoke_membership'),
    url(r'^teams/invitations/(?P<invite_id>[0-9]+)/$', views.teams.decide_invitation, name='decide_invitation'),

    url(r'^boards/(?P<board_id>[0-9]+)/$', views.boards.detail, name='detail'),
    url(r'^boards/create$', views.boards.create_board, name='create_board'),
    url(r'^boards/(?P<board_id>[0-9]+)/history/', views.boards.board_history, name='board_history'),
    url(r'^boards/(?P<board_id>[0-9]+)/edit/', views.boards.edit_board, name='edit_board'),
    url(r'^boards/(?P<board_id>[0-9]+)/permissions/', views.boards.edit_permissions, name='edit_permissions'),
    url(r'^boards/(?P<board_id>[0-9]+)/evidence/add', views.evidence.add_evidence, name='add_evidence'),
    url(r'^evidence/(?P<evidence_id>[0-9]+)/sources/add', views.evidence.add_source, name='add_source'),
    url(r'^evidence/(?P<evidence_id>[0-9]+)/edit/', views.evidence.edit_evidence, name='edit_evidence'),
    url(r'^hypotheses/(?P<hypothesis_id>[0-9]+)/edit/', views.hypotheses.edit_hypothesis, name='edit_hypothesis'),
    url(r'^evidence/(?P<evidence_id>[0-9]+)/sources/(?P<source_id>[0-9]+)/tag', views.evidence.toggle_source_tag, name='tag_source'),
    url(r'^evidence/(?P<evidence_id>[0-9]+)', views.evidence.evidence_detail, name='evidence_detail'),
    url(r'^boards/(?P<board_id>[0-9]+)/hypotheses/add', views.hypotheses.add_hypothesis, name='add_hypothesis'),
    url(r'^boards/(?P<board_id>[0-9]+)/evidence/(?P<evidence_id>[0-9]+)/evaluate$', views.boards.evaluate, name='evaluate'),
    url(r'^boards/(?P<board_id>[0-9]+)/(?P<dummy_board_slug>[A-Za-z0-9\-]+)/$', views.boards.detail, name='detail_slug'),
    url(r'^about$', views.site.about, name='about'),

    # JSON API
    url(r'^api/boards/$', views.boards.board_search, name='board_search'),
]
