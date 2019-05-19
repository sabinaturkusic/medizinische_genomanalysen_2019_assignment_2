#! /usr/bin/env python3

import vcf  #sudo pip3 install PyVCF or via project in pycharm

__author__ = 'Sabina Turkusic'


class Assignment2:
    
    def __init__(self, chr21_file, chr22_file):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        self.chr21_file = chr21_file
        self.chr22_file = chr22_file
        self.vcf_reader1 = vcf.Reader(open(self.chr21_file, "r"))
        self.vcf_reader2 = vcf.Reader(open(self.chr22_file, "r"))


    def get_average_quality_of_file(self):
        #record = next(self.vcf_reader2)
        #print(record.QUAL)
        quality_list = []
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                quality_list.append(record.QUAL)

        average_quality = sum(quality_list) / float(len(quality_list))
        print("The average PHRED quality is:", average_quality)


    def get_total_number_of_variants_of_file(self):
        total_number = 0
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                total_number += 1
        print("The total number of variants is:", total_number)
    
    
    def get_variant_caller_of_vcf(self):
        variant_caller = []
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                info = record.INFO["callsetnames"]
                for i in range(len(info)):
                    variant_caller.append(info[i])
        print("Variant caller of vcf:", set(variant_caller))
        
        
    def get_human_reference_version(self):
        ref_list = []
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                info = record.INFO ["difficultregion"]
                reference_version = info[0][0:4]
                print("The human reference version is:", reference_version)
                break

        
    def get_number_of_indels(self):
        indel_counter = 0
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_indel:
                    indel_counter += 1
        print("The number of INDELs is:", indel_counter)


    def get_number_of_snvs(self):
        snv_counter = 0
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter += 1
        print("The number of SNVs is:", snv_counter)

        
    def get_number_of_heterozygous_variants(self):
        heterozygote_counter = 0
        with open(self.chr22_file) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.num_het:
                    heterozygote_counter += 1
        print("The number of heterozygote variants is:", heterozygote_counter)

    
    def merge_chrs_into_one_vcf(self):
        vcf_read = vcf.Reader(open(self.chr21_file))
        vcf_write = vcf.Writer(open("merge.vcf", "w+"), vcf_read)
        for record in vcf_read:
            vcf_write.write_record(record)

        vcf_read_1 = vcf.Reader(open(self.chr22_file))
        vcf_write_1 = vcf.Writer(open("merge.vcf", "a"), vcf_read_1)
        for record in vcf_read_1:
            vcf_write_1.write_record(record)

        line_counter = 0
        with open("merge.vcf") as merge:
            for line in merge:
                line_counter += 1

        print("A new file has been created and the total number of lines in new vcf file is:", line_counter)

    
    def print_summary(self):
        print("Print all results here")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()

    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr21_new.vcf", "chr22_new.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



