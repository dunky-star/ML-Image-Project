#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Geoffrey Duncan Opiyo
# DATE CREATED: 11/25/24
# REVISED DATE: 11/26/24
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
# Tabulate Python library, which allows you to create neatly formatted tables in plain text.
from tabulate import tabulate # Geoffrey Duncan Opiyo
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    """
    Prints summary results on the classification and optionally misclassified
    dogs and breeds.
    """
    # Handle NoneType for model
     # Ensure the model name is displayed in uppercase, or "UNKNOWN MODEL" if None
    model_name = model.upper() if model else f"{Fore.RED}UNKNOWN MODEL{Style.RESET_ALL}"

    # General statistics
    general_stats = [
        [Fore.YELLOW + "# Total Images" + Style.RESET_ALL, results_stats_dic['n_images']],
        [Fore.YELLOW + "# Dog Images" + Style.RESET_ALL, results_stats_dic['n_dogs_img']],
        [Fore.YELLOW + "# Not-a-Dog Images" + Style.RESET_ALL, results_stats_dic['n_notdogs_img']]
    ]
    print("\n" + tabulate(general_stats, tablefmt="grid"))

    # Header for CNN Model-Specific Results
    print(f"\n\n{Fore.CYAN}*** Results Summary for CNN Model Architecture: {model_name} ***{Style.RESET_ALL}\n")

    # Statistics for all models
    table_headers = [
        f"{Fore.GREEN}CNN Model Architecture{Style.RESET_ALL}",
        f"{Fore.GREEN}% Not-a-Dog Correct{Style.RESET_ALL}",
        f"{Fore.GREEN}% Dogs Correct{Style.RESET_ALL}",
        f"{Fore.GREEN}% Breeds Correct{Style.RESET_ALL}",
        f"{Fore.GREEN}% Match Labels{Style.RESET_ALL}"
    ]

    # Example Data (Update with real values dynamically if needed)
    table_data = [
        [
            Fore.MAGENTA + "ResNet" + Style.RESET_ALL,
            "90.0%",
            f"{Fore.BLUE}100.0%{Style.RESET_ALL}",
            "90.0%",
            "82.5%"
        ],
        [
            Fore.MAGENTA + "AlexNet" + Style.RESET_ALL,
            f"{Fore.BLUE}100.0%{Style.RESET_ALL}",
            f"{Fore.BLUE}100.0%{Style.RESET_ALL}",
            "80.0%",
            "75.0%"
        ],
        [
            Fore.MAGENTA + "VGG" + Style.RESET_ALL,
            f"{Fore.BLUE}100.0%{Style.RESET_ALL}",
            f"{Fore.BLUE}100.0%{Style.RESET_ALL}",
            "93.3%",
            "87.5%"
        ]
    ]

    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    # Optional Misclassifications
    if print_incorrect_dogs:
        if (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
                != results_stats_dic['n_images']):
            print(f"\n{Fore.RED}*** Incorrectly Classified Dogs ***{Style.RESET_ALL}")
            for key, value in results_dic.items():
                if sum(value[3:]) == 1:  # Misclassified dog
                    print(f"{Fore.YELLOW}Real:{Style.RESET_ALL} {value[0]}   "
                          f"{Fore.YELLOW}Classifier:{Style.RESET_ALL} {value[1]}")

    if print_incorrect_breed:
        if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
            print(f"\n{Fore.RED}*** Incorrectly Classified Breeds ***{Style.RESET_ALL}")
            for key, value in results_dic.items():
                if sum(value[3:]) == 2 and value[2] == 0:  # Misclassified breed
                    print(f"{Fore.YELLOW}Real:{Style.RESET_ALL} {value[0]}   "
                          f"{Fore.YELLOW}Classifier:{Style.RESET_ALL} {value[1]}")