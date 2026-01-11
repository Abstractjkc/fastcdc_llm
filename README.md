
# Fast CDC for LLM

实现针对 LLM 的 CDC(Content Defined Chunking) 算法 fastcdc，
传统的 cdc 内容单元是字节 (byte), gear table 大小仅为 256。
想针对 LLM 实现 cdc 算法，tokenizer 词表大小很大。
因此只需要根据词表大小生成一个新的 gear table 即可。

## TODO List
- [x] 根据词表大小生成 gear table
- [] 实现 fastcdc 算法

## Environment Setup

```bash
pip install -r requirements.txt
```
## Reference Materials

- [FastCDC implementation in Rust](https://github.com/nlfiedler/fastcdc-rs)

- [fastcdc tutorial](https://joshleeb.com/posts/fastcdc.html)

- [gear hashing tutorial](https://joshleeb.com/posts/gear-hashing.html)