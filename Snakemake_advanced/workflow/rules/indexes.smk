rule download_reference:
    output: "resources/indexes/{genome}/{genome}.fa.gz"
    log: "logs/indexes/{genome}/{genome}.fa.gz.log"

    shell:
        "wget -O {output} http://hgdownload.soe.ucsc.edu/goldenPath/{wildcards.genome}/bigZips/{wildcards.genome}.fa.gz &> {log}"

rule bowtie2_index:
    input:
        reference=ancient(rules.download_reference.output)
    output:
        multiext(
            'results/indexes/{genome}/{genome}',
            '.1.bt2','.2.bt2','.3.bt2','.4.bt2','.rev.1.bt2','.rev.2.bt2',
        )
    log: "logs/indexes/{genome}.log"
    benchmark: "benchmarks/indexes/{genome}.txt"

    threads: config['bowtie2_index']['threads']
    params:
        extra=config['bowtie2_index']['extra']
    # custom conda env file with another bowtie2 version
    conda: "../envs/bowtie.yaml"
    wrapper: "0.74.0/bio/bowtie2/build"
