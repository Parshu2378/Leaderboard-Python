from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from leaderboard.models import User, Winner
from leaderboard.serializers import UserSerializer, WinnerSerializer
from django.shortcuts import render


@api_view(['GET'])
def dashboard(request):
    # Fetch leaderboard data
    leaderboard = User.objects.order_by('-points')

    # Fetch winners data
    winners = Winner.objects.select_related('user')

    # Prepare grouped data by score
    grouped_data = {}
    users = User.objects.all()
    scores = users.values_list('points', flat=True).distinct()

    for score in scores:
        score_users = users.filter(points=score)
        avg_age = score_users.aggregate(Avg('age'))['age__avg']
        grouped_data[score] = {
            "names": list(score_users.values_list('name', flat=True)),
            "average_age": avg_age,
        }

    # Render data to the template
    return render(request, 'dashboard.html', {
        'leaderboard': UserSerializer(leaderboard, many=True).data,
        'winners': WinnerSerializer(winners, many=True).data,
        'grouped_data': grouped_data,
    })


@api_view(['GET'])
def get_leaderboard(request):
    users = User.objects.order_by('-points')
    return Response(UserSerializer(users, many=True).data)


@api_view(['GET'])
def get_winners(request):
    winners = Winner.objects.select_related('user').order_by('-timestamp')
    return Response(WinnerSerializer(winners, many=True).data)


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User added', 'user': serializer.data})
    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def update_points(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.points += int(request.data.get('points', 0))
        user.save()
        return Response({'message': 'Points updated', 'points': user.points})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


@api_view(['DELETE'])
def delete_user(request):
    user_id = request.data.get('id')
    if not user_id:
        return Response({'error': 'User ID is required'}, status=400)
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'message': 'User deleted'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


@api_view(['GET'])
def get_user_details(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return Response(UserSerializer(user).data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


@api_view(['GET'])
def grouped_by_score(request):
    users = User.objects.all()
    grouped_data = {}
    scores = users.values_list('points', flat=True).distinct()

    for score in scores:
        group = users.filter(points=score)
        avg_age = group.aggregate(Avg('age'))['age__avg']
        grouped_data[score] = {
            "names": list(group.values_list('name', flat=True)),
            "average_age": avg_age,
        }

    return Response(grouped_data)


def documentation(request):
    return render(request, 'documentation.html')