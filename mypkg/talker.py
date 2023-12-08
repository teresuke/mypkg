import rclpy
from rclpy.node import Node
from person_msgs.msg import Query

def cb(request,response):
    if request.name == "上田隆一":
        response.age = 44
    else:
        response.age = 255

    return response
    
rclpy.init()
node = Node("talker")
srv = node.create_survice(Query, "query", cb)
rclpy.spin(node)
