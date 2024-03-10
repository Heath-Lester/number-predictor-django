"""View for Winning Sets"""
from django.views.generic.base import View


class WinningSets(View):
    """Winning Sets"""

    def list(self, request):
        """Handles GET requests for all Winning Sets"""
