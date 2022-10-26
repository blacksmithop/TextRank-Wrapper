# Welcome to MkDocs

 A wrapper to make using [pytextrank](https://github.com/DerwenAI/pytextrank/) simpler


## Usage

```python
insights = ['50%, if &lt;50%, I use Pembrolizumab combo even if PD-L1 negative.', 'Academic SL expressed that KN048 PFS2 data confirmed the use of Pembrolizumab monotherapy and Pembrolizumab + Chemo Therapy as 1st line therapy in RM HNSCC.', 'While P + A and N + I are considered SoC in 1L RCC, A + A is not at the same level.', '1L RCC: based in the published data, the Avelumab + Axitinib combination is not considered as a therapeutic option for the SL.', 'The treatment for adenocarcinoma with IO in combination with Chemo Therapy, would be for patients selected by PD-L1 expression (considering the results of CM649 and KN590)', 'It is going to impact my patients who I would have included in the clinical trials like LEAP 002 study (Pembrolizumab plus Lenvatinib).', 'I look at PD-L1 and make sure I have NGS in patients.', 'HCC, KN - 524 SL agrees that the combination of Lenvatinib and Pembrolizumab (KN - 524) looks promising in HCC and it could play a major role across GI cancers.', 'KN426_The efficacy results in the favorable risk group are not enough to make P + A the SoC in 1L for this patients population.', 'It might indicate that there might not be a survival benefit in this patient group for Pembrolizumab + Chemo arm.']
```

```python
tr = TextRank(insights=insights)
print(tr.summarize())
```