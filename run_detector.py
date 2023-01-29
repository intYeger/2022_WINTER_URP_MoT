import argparse
from yolov7.detect import detect
from draw import draw
from find_team import find_team
from tragectory_converter import tragectory_converter
from convert_yolov7_to_coco import convert_yolov7_to_coco
from association import transform_det, tracking


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    parser.add_argument('--detect-offside', action='store_true', help='show offside line')
    parser.add_argument('--stopover', default='runs/detect/exp', help='save result')
    opt = parser.parse_args()
    print(opt)

    # 1. yolo detect
    # detect(opt)

    # 2. trajectory_convert
    # tragectory_converter(opt)
    
    # 3. team classify
    # find_team(opt)

    # gt = convert_yolov7_to_coco('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp/labels', 'C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp')
    # tracking('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp', gt, True)

    # gt = convert_yolov7_to_coco('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp/labels', 'C:/Users/ys102/Desktop/URP/soccernet/path/to/SoccerNet/tracking/train/SNMOT-060/img1')
    det = convert_yolov7_to_coco('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp5/labels', 'C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp5')
    tracking('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp5', det, True)

    # # 4. draw
    # draw('C:/Users/y/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp5', False, gt)
    # draw('C:/Users/y/Desktop/URP/test', True, [1])
    # draw('C:/Users/ys102/Desktop/URP/2022_WINTER_URP_MoT/runs/detect/exp', True, gt)
    
    
    
    # 5. +@ find pass frame
