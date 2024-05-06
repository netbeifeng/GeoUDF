import os
# path = "/home/featurize/data"
# output_path = "/home/featurize/processed"
# # categories = ["door", "eyeglasses", "refrigerator", "laptop", "stapler", "washing_machine", "oven"]
# categories = ["laptop"]

# tasks = []


# for category in categories:
#     cate_path = os.path.join(path, category)
#     models = os.listdir(cate_path)
#     for model in models:
#         model_path = os.path.join(cate_path, model, "super_dense_pcl_seq")
#         files = os.listdir(model_path)
#         output_file = os.path.join(output_path, category, model, "super_dense_pcl_seq")
#         if not os.path.exists(output_file):
#             os.makedirs(output_file)
        
#         for file in files:
#             file_path = os.path.join(model_path, file)
#             output_file_path = os.path.join(output_file, file)
#             tasks.append("python eval_rec.py --res 128 --input '{}' --output '{}'".format(file_path, output_file_path))
            
# print("Total tasks: ", len(tasks))

# from tqdm import tqdm
# try:
#     for task in tqdm(tasks):
#         os.system(task)
# except KeyboardInterrupt:
#     print("Interrupted")
#     exit(0)
        
import time
start = time.time()
cmd1 = "python eval_rec.py --res 128 --input '/home/featurize/data/door/0008/super_dense_pcl_seq/00000000.ply' --output './x128_wm.ply'"
os.system(cmd1)
end = time.time()
print("Time taken: ", end - start)
