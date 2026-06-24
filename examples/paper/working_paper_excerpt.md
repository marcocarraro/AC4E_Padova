# Working Paper Excerpt For Referee Exercise

This is a synthetic teaching example. It is not a real paper.

## Title

Remote Work And Local Service Employment: Evidence From A City-Level Pilot

## Abstract

We study whether remote work reduces employment in local service sectors. Using
a difference-in-differences design around a 2020 remote-work policy pilot in 12
treated cities, we find that local service employment fell by 8 percent. The
results are robust and imply that remote work permanently reduces urban service
demand.

## Introduction

Remote work has changed the spatial organization of economic activity. This
paper estimates the effect of a remote-work policy pilot on local service
employment. The treated cities adopted remote-work guidance in March 2020. We
compare them with 18 cities that did not adopt guidance until later.

The contribution is twofold. First, we provide causal evidence that remote work
reduces local service employment. Second, we show that the effect is permanent,
which has implications for urban policy.

## Empirical Strategy

We estimate:

```text
y_ct = alpha_c + gamma_t + beta Treat_c x Post_t + epsilon_ct
```

where `y_ct` is log local service employment in city `c` and month `t`.
`Treat_c` equals one for pilot cities and `Post_t` equals one after March 2020.
Standard errors are clustered by city.

The identifying assumption is that treated and control cities would have followed
parallel trends in the absence of treatment. Figure 1 shows employment trends.
The treated cities have somewhat faster service-sector growth before March 2020,
but the difference is small.

## Results

Table 1 reports the main estimates.

| Column | Outcome | Controls | Estimate | Standard error |
| --- | --- | --- | ---: | ---: |
| 1 | Log service employment | City and month FE | -0.021 | 0.018 |
| 2 | Log service employment | + city linear trends | -0.034 | 0.020 |
| 3 | Log service employment | + industry mix controls | -0.081 | 0.027 |

The estimate in column 2 implies that remote work reduced local service
employment by about 8 percent. This effect is statistically significant at the 1
percent level and economically large.

## Robustness

The results are robust to adding controls. We also checked alternative outcomes,
but do not report them for space reasons.

## Conclusion

Remote work permanently reduced local service employment in treated cities. The
evidence suggests that cities should subsidize downtown service firms to offset
the negative shock from remote work.

