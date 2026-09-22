<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0718.txt",
      "sha256": "075b003887cd4078fd5eca4e6200d3361cb23654329533cfec55a7c136b6a5d2",
      "bytes": 13570
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4aa46fcbb80796897f91a1d057c9c4728bca90005f33670a41f0510f03623354",
      "bytes": 1628
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "253e9b5288386051c82bc2373ba82835eacd1d4a307dbac220c69208d60acf41",
      "bytes": 208264
    },
    {
      "path": "characters/Baekhwi.md",
      "sha256": "a16ab6155892300c06d0a384ada2cbdd90f4338b939111e220aba7be784ebbd6",
      "bytes": 493
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "bc554483dab4dd82ccf0a560055864a84affe0741b2802f3fea8e19acc23c63a",
      "bytes": 935
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "0f50731291efbb63bb431434c8be218c991222ad899aae1fdb48b55d0373012b",
      "bytes": 899
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b7431239f01aeeb7d88ce58144ded2550596733dd9ffeb68e4218344582d3d96",
      "bytes": 553
    },
    {
      "path": "characters/Guardian Spirit.md",
      "sha256": "6c4b6daf068417ea111556d3339f44212f5ddbe21046ecfe9d39b97793281ddd",
      "bytes": 645
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ff0c9738f5f280ea9289a2b87e61d1e5398619293426abd8459a1f09a112f940",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "659bfa6d80d64fe3016f850ef3aab210b69fe808f33ec378cae243841f806ce7",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "917daeb8ddc099d3e0455b02d698c49d661b9f4329ba4c09109a120837d4f2b9",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ff357bd805d45735129f367b288d5b4fb85de4c748a7007cc6eba222067c2581",
      "bytes": 218760
    }
  ],
  "estimated_tokens": 11368
}
-->

# Durable State Update — Chapter 718

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 718. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 718. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 718,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 718,
    "continuity_sources": [718],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Nanman Beast Palace is being rebuilt after the rift disaster, whose demonic qi has disappeared but whose casualties and social aftermath remain.",
    "The Beast Miao King is hiding in a dilapidated shrine in the Outer Palace after disappearing for two days.",
    "Nanman's leadership abandoned its search after Jeok Cheongang ordered them to calm the people and promised to intervene after midnight if necessary.",
    "Jin Taekyung has fully recovered after seven days and nights of rest and a level-up.",
    "The Seven Miao Tigers guard the Beast Miao King, and Wonhu allowed Jin to pass through to meet him.",
    "The Beast Miao King is overwhelmed by grief over failing to protect the Nanman tribespeople and Baeksang.",
    "The Beast Miao King is questioning whether he is qualified to remain Palace Lord.",
    "The Seven Miao Tigers regard Jin as Nanman's benefactor because he saved them in the underground prison."
  ],
  "continuity_sources": [
    717
  ],
  "open_questions": [
    "What does the Beast Miao King identify as the greatest source of his pain?"
  ],
  "safe_through": 717,
  "temporary_decisions": [
    "Render 대형 as Big Brother when the Seven Miao Tigers address Wonhu.",
    "Retain Old Master for 노야 when Jin addresses Jeok Cheongang.",
    "Retain established renderings of Flame Divine Palm, Flame-Extinguishing Divine Fist, Dance of the Fire God and Demon, Solar Fist, Force, Skill, and great fiend for 대마두.",
    "Render 남만당 as Nanman Party.",
    "Render 각주 as Pavilion Master when Taishan addresses Jin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 퀘스트              | **Quest**                      |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백휘 | **Baekhwi** | Baeksang's deceased only child. |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 백휘 | father_to_deceased_child | Hwi | emotionally charged and possessive | Baeksang directly invokes his deceased child's name while confronting Jin. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 백상 | 부족장 | Palace Lord to subordinate tribal chieftain | you | cold, final, and detached | Baeksang refuses the chieftain's plea for mercy and tells him not to consider the exchange unjust. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 수호령 | 적천강 | guardian_spirit_to_legendary_martial_master | old human | terse and contemptuous | The guardian spirit addresses Jeok as 늙은 인간 while recognizing that his essence has not changed. |

## Listed compact profiles

### Baekhwi.md

# Baekhwi (백휘)

- **Safe through:** Chapter 713
- **Aliases:** None
- **Role:** Baekhwi was Baeksang's only child, would have become the Beast Miao King's son-in-law, and was killed without leaving a corpse during the Great Snow Mountain battle.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Baeksang's only child; would have been the Beast Miao King's son-in-law if he had lived.

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 716
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 717
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people who is currently hiding in a dilapidated shrine within the Outer Palace while grieving those he failed to protect.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 717
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Guardian Spirit.md

# Guardian Spirit (수호령)

- **Safe through:** Chapter 713
- **Aliases:** None
- **Role:** The Guardian Spirit was a divine-beast-like tiger that sacrificed itself to seal the rift and was killed after becoming corrupted.
- **Personality:** The Guardian Spirit was self-sacrificing and chose death rather than allow its corruption to continue.
- **Voice:** The Guardian Spirit communicates through roars and terse cries; no sustained speech is established.
- **Relationships:** The Guardian Spirit asked Jin Taekyung and Jeok Cheongang to kill it if corruption overcame it.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 717
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 717
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 717
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃718화



“그토록 많은 이들이 죽었음에도, 내 마음속에는 백상 한 사람에 대한 슬픔이 가장 크게 자리 잡고 있었다는 것이다.”

귓가를 파고드는 나직한 목소리. 잠시 침묵하던 나는 입을 열었다.

“그래서 떠난 겁니까. 자신의 그런 마음이 잘못되었다고 생각해서?”

“남만야수궁의 궁주가 된다는 것은…… 다른 무엇보다 이 땅과 부족민들을 우선시해야 한다는 뜻이다. 하지만 나는 사사로운 감정에 사로잡히고 말았지.”

천년거석처럼 커다란 등이 보인다. 그러나 긴 세월 동안 남만을 지탱해 왔을 거인의 뒷모습은, 지금 이 순간 어린아이처럼 초라해 보였다.

“마지막으로 백상과 마주했을 때, 내가 무슨 생각을 떠올렸는지 아느냐?”

충분히 짐작한다. 하지만 구태여 말하지 않았다.

누구보다 그에 관하여 잘 알고, 가장 고통스러워한 이가 내 앞에 있었으니까.

“어떻게든 살리고 싶더군.”

“…….”

“그 참혹한 광경 속에서도, 나를 비롯한 이 땅의 모두를 배신한 백상 그 녀석을 구하여 멀리 도망치게 하고 싶었다.”

비록 피는 섞이지 않았지만, 혈육이나 다름없는 의형제.

야수묘왕은 어떻게든 백상을 구명하고 싶었을 것이다.

죽은 줄로만 알았던 자식을 인질로 붙잡힌 채, 암천의 사냥개 노릇을 해 왔던 그에게 면죄부를 내려 주고 싶었을 것이다.

그러나 그것을 거부한 것은, 백상 본인이었다.

“아마 그 녀석도 알았겠지. 내가 망설이고 있다는 것을. 그래서 그런 선택을 한 것이겠지.”

야수묘왕의 뇌까림이 공허하게 흩어진다.

그 목소리에 담긴 감정은 목숨보다도 아꼈던 의제(義弟)의 숨통을 제 손으로 끊을 수밖에 없던 것에 대한 비통함이었고, 사사로운 감정으로 궁주로서의 본분을 저버린 자신에 대한 자책이었다.

“병든 나무 한 그루로 인하여 숲이 죽었다. 한데 숲을 돌보아야 하는 숲지기는 이미 쓰러져 버린 병든 나무 앞을 서성이고 있구나. 너는 그런 자를 숲지기라 부를 수 있겠느냐?”

조용히 야수묘왕의 이야기를 듣고 있던 내가, 긴 침묵을 깨트리며 입을 열었다.

“야율 대협, 이건 진짜 진심으로 묻는 건데…….”

나도 모르게 흐려지는 말꼬리.

솔직히 지금 이 순간조차도 이런 말을 해도 되나 싶다. 하지만 저 멘탈이 나가 버린 숲지기를 어떻게든 일으켜 세워야 한다.

아주 조금, 어쩌면 많이 선을 넘더라도.

“혹시 병신이세요?”

“……!”

야수묘왕의 뒷모습에서 감출 수 없는 동요가 느껴진다. 그러나 기왕 내친걸음, 나는 거침없이 말을 이었다.

“궁주는 뭐 천지신명이라도 됩니까? 사람으로서의 감정도 없어요?”

“너…….”

“까놓고 말해 봅시다. 당장 평생을 함께한 혈육 같은 사람이 죽었는데, 이 세상 누가 멀쩡할 수 있습니까? 단지 다른 사람들이 죽었다고 더 슬퍼해요?”

와르르 쏟아지는 직설적인 말들에 잠시 침묵하던 야수묘왕이 입을 열었다.

“진태경, 너 역시 말이냐?”

나는 고개를 끄덕였다.

“그게 당연한 거 아닙니까. 저 같은 새끼가 뭐 대단한 놈이라고.”

“…….”

“주위에서 협객이니, 대협이니 치켜세워 줘도 결국 사람입니다. 궁주라고 해서 다르겠습니까.”

한 치의 망설임도 없는 대답에, 드넓은 등이 움직였다.

스윽.

서서히 돌아선 고개.

내가 이 낡은 사당에 발을 디딘 이래 처음으로 마주한 야수묘왕의 안색은 초췌하기 그지없었다.

“그들 역시 내가 지켜야 할 남만의 백성들이었다.”

“그래서 지켰잖습니까. 배반자로 낙인찍힌 뒤에도 위험을 무릅쓰면서까지 돌아왔잖습니까. 또 다른 수많은 이들을 구할 수 있었던 건 그 덕분입니다.”

나는 조용히 말을 이었다.

“이미 병든 나무들은 쓰러졌고, 숲은 아직 죽지 않았습니다. 오히려 그 어느 때보다 숲지기를 필요로 하고 있어요.”

이번 일로 많은 이들이 희생되었다. 하지만 아이러니하게도 남만은 더욱 부강해질 것이다.

남만이라는 이 거대한 숲에서 병든 나무는 백상 한 사람뿐만이 아니었으니까.

‘또 다른 부족장들. 아니, 배반자들.’

백상이 자식을 위해 암천과 손을 잡았다면, 그들은 단지 일신의 안위와 권세를 위해 백상을 따랐다.

하여 그들이야말로 진작 베어 내야 했을 나무들이다. 탐욕이란 병에 걸린 나무들.

그렇게 무려 스무 명이 넘는 부족장들이 탐욕에 취해 제 몸에 달린 나뭇가지를 흔들었고, 그로 인하여 무수한 나뭇잎이 핏물 위를 뒹굴었으나 숲은 죽지 않았다.

아니, 남만야수궁이라는 하나의 깃발 아래에서 더욱더 하나 되어 번성할 것이다.

그리고 모든 남만인의 앞에서 그 깃발을 들어 올릴 수 있는 이는, 단 한 사람뿐이었다.

“이만 돌아가시죠. 그래야 저 부자(父子)도 마음 편히 쉴 수 있지 않겠습니까.”

목소리는 야수묘왕을 향한 것이었지만, 지금 내 눈동자는 다른 곳을 바라보고 있었다.

내 시선이 어디에 머무는지 알아차린 야수묘왕이 나직이 물었다.

“알고 있었더냐.”

“처음 들어오자마자 눈에 띄었습니다. 사당 안에 있는 거라곤 죄다 먼지투성이인데, 저것만 멀쩡하더라고요.”

나는 천천히 걸음을 옮겨 나아갔다.

색 바랜 벽화와 정체를 알 수 없는 수십여 개의 석상 사이에, 지난번에는 볼 수 없었던 두 개의 위패(位牌)가 놓여 있었다.

이름조차 적혀 있지 않은 두 개의 위패.

하지만 나는 저 위패의 주인들이 누구인지 이미 알고 있다.

‘백상. 백휘.’

이 위패를 손수 만들었을 이조차 차마 새겨 넣을 수 없었을 그 이름들을 마음속으로 뇌까렸다. 그리고 엎드려 절했다.

한 번. 또 한 번.

그렇게 두 번의 절을 마치고 돌아섰을 때, 굳어 있는 야수묘왕의 얼굴이 나를 기다리고 있었다.

“왜 그런 눈으로 보십니까?”

“……의외라서.”

“제가 뭐, 위패라도 엎을 줄 아셨나 보네요.”

“너라면 그럴 수 있다. 적어도 백상, 그 녀석이 지은 죄를 생각한다면 더더욱.”

젠장. 그건 그렇지.

지금까지의 일을 생각한다면 내가 백상의 위패를 반으로 쪼갠 뒤 침을 뱉어도 정당방위다.

하지만…….

“그냥. 그냥 이러고 싶었습니다. 단지 그뿐이에요.”

뭘까. 이 더러우면서도 씁쓸한 기분은.

다시 고개를 돌려 위패를 바라본 나는, 문득 지금 이 감정을 알 것 같기도 했다.

그건 어쩌면 동정이나 공감이라 불려야 할 무언가인지도 모른다.



‘늦었다. 나는 돌이킬 수 없는 길을 걸었고, 결코 멈추지 않을 것이다.’



어두컴컴한 뇌옥에서 들었던 목소리가 언뜻 귓가에 울려 퍼지는 듯했다.

나는 이름 한 글자 적혀 있지 않은 위패를 바라보며 들리지 않을 물음을 던졌다.

‘만약 내가 당신이었다면, 나는 어떤 길을 걸었을까.’

그리고 그 물음에 대한 답은 어디서도 들려오지 않았다.

위패가 아닌 내 마음 깊숙한 곳에서조차. 다만 문득 그런 생각이 들었다.

만약 내세(來世)라는 것이 존재한다면, 저 찢어 죽여도 시원치 않을 놈이 이번과는 다른 평범한 삶을 살았으면 좋겠다고.

누구도 잃지 않고, 누구도 희생시키지 않는 그런 평온한 삶 속에서 그토록 그리워하던 자식과 함께했으면 좋겠다고.

‘젠장. 저놈 때문에 죽은 사람이 몇인데.’

안다. 이 세상에 사연 없는 악당은 없다는 것 정도는.

하지만 이토록 기분이 더러운 이유는 간단하다.

어쩌면 나 역시 백상과 같은 길을 걸었을지도 모르니까.

그가 자신에게 주어진 상황 속에서 얼마나 몸부림쳤는지 충분히 짐작하고 있으니까.

그렇기에 내가 할 수 있는 말이라고는, 고작 이 정도가 전부였다.

“……거기선 죄짓지 마라. 이 시부럴 새끼야.”

작게 중얼거린 그때, 사당의 문틈 사이로 흘러들어 온 불그스름한 빛이 두 개의 위패를 비추었다.

마치 그것으로 대답을 대신하겠다는 듯이.

그리고 다음 순간, 굵직한 목소리가 내 귓가를 파고들었다.

“벌써 해가 지고 있구나.”

끼익.

낡은 바닥이 비명을 지른다. 마침내 가부좌를 풀고 자리에서 일어난 거한이, 담담한 눈빛으로 나를 응시했다.

“지금 곧장 내궁으로 향한다면, 저녁 식사 정도는 함께 할 수 있겠지.”

“……!”

“가자. 더 늦지 않게 돌아가야겠으니.”

그런 야수묘왕을 바라보던 나는 피식 웃으며 고개를 끄덕였다.

남만의 숲지기가 돌아왔다.



* * *



이틀이 지났다.

말도 없이 사라졌던 궁주가 다시 돌아오자 혼란에 빠져 있던 수뇌부는 순식간에 안정을 되찾았고, 모두의 권유에 짧은 휴식을 취한 야수묘왕은 이튿날 나를 호출했다.

아니, 정확히는 적천강과 나를.

그리고 칠 주야 만에 급조한 회의실에 도착한 적천강은, 자리에 앉아 있던 야수묘왕을 보자마자 이렇게 말했다.

“많이 컸네, 우리 묘왕이. 상석에 다 앉아 있고.”

“……헉. 죄송합니다. 습관적으로 그만.”

“아니다. 충분히 이해한다. 그러니 버릇없는 놈을 보면 화염신장을 날리는 노부의 습관도 이해하거라.”

쉬쉭!

정마대전 때 이미 그 습관을 겪어 본 적이 있는 야수묘왕이다.

붕대를 칭칭 감은 몸을 잽싸게 움직여 상석을 비운 그가 공손히 자리를 가리켰다.

“앉으십시오, 적 노.”

“허어, 괜찮다. 몸도 불편한 놈이 뭘 이렇게까지.”

“…….”

“됐으니 그만 앉아라. 대가리에 피도 안 마른 놈이 오라 가라 한 건 마음에 안 들지만, 우선은 맘대로 지껄여 봐.”

간만에 겪는 깡패식 화법에 혼란스러워하는 야수묘왕을 위해, 내가 점잖게 입을 열었다.

“그냥 말씀하시면 됩니다. 저 정도면 경청하시겠다는 뜻이에요.”

“……그럼 적 노, 이 후배가 한 말씀 올려도 되겠습니까?”

“되묻는 거 되게 싫어하십니다. 아직 몸도 성치 않으신데 험한 꼴 당하기 싫으시면 바로 말씀하세요.”

“……알았다.”

예전 기억과는 달리 한참 젊어진 적천강의 모습을 힐끔거린 야수묘왕이 조심스럽게 입을 열었다.

“이렇게 적 노까지 모신 것은 한 가지 중대 사안에 관하여 여쭙기 위해섭니다.”

“중대 사안?”

“예. 그렇습니다.”

“지금까지 뒷수습도 원만히 되어 가는 것으로 아는데. 혹 암천의 꼬리라도 밟았느냐?”

“그랬다면 좋았겠지만, 안타깝게도 아닙니다. 하지만 다른 의미로는 그보다 머리 아픈 문제라…….”

“서두가 길다. 네놈 명줄 짧아지기 전에 본론부터 말해라.”

이 양반 여전하시네.

딱 그 눈빛으로 적천강을 바라본 야수묘왕이 품에서 무언가를 꺼내 탁자 위에 올려놓았다.

툭.

두꺼운 천에 싸여 있는 무언가. 하지만 나를 비롯한 이 자리의 모두는 그 너머로 흘러나오는 불길한 기운을 느낄 수 있었다.

그리고 순식간에 무거워진 공기 속, 적천강이 침음성처럼 중얼거렸다.

“……마기(魔氣)?”

야수묘왕이 굳은 얼굴로 고개를 끄덕였다.

“맞습니다. 그것도 아주 순수하고 강력한 마기지요. 남만의 다른 이에게 맡길 수 없어 후배가 직접 지니고 있었습니다.”

그들의 목소리가 메아리처럼 멀게만 느껴진다.

나는 이 마기의 근원이 어디이며, 저 천 안에 숨겨진 것이 무엇인지 알 것 같았다.

더불어 짙은 어둠 속에서 울려 퍼지던 한 존재의 마지막 포효가 귓가에서 울려 퍼졌다.

“신석(神石)이군요. 수호령이 지니고 있던.”

“네 짐작대로다. 비록 이제는 신석이 아니게 되어 버렸지만.”

스륵.

착잡한 어조로 대답한 야수묘왕이 천을 걷자, 따스하고 눈부신 광휘 대신 혼탁한 어둠을 머금은 돌이 모습을 드러냈다.

균열로부터 흘러나오던 마기를 모조리 흡수한 그것은 이제 마석(魔石)이라 불려야 할 무언가였고, 이를 바라보는 야수묘왕의 눈빛은 깊게 가라앉아 있었다.

“지금은 내가 마기를 억누르고 있으나, 언제까지고 지금처럼 내버려 둘 수는 없는 법. 하여 이것의 처우를 논의하고자 너와 적 노를 청했다.”

그 순간.

띠링.

눈앞의 혼탁한 어둠과는 상반되는 맑은 종소리와 함께, 홀로그램 창이 허공에 떠올랐다.



퀘스트, [타락한 신물]을 수락하시겠습니까?

Y / N
```

## Final English reading copy

```markdown
# Chapter 718

“Despite so many people dying, the grief that occupied the greatest place in my heart was for Baeksang alone.”

The low voice pierced my ears. After a brief silence, I opened my mouth.

“So that’s why you left? Because you thought those feelings of yours were wrong?”

“To become the Palace Lord of the Nanman Beast Palace means putting this land and its tribespeople before anything else. But I became trapped by my personal feelings.”

I could see his enormous back, like a thousand-year-old megalith. Yet the back of the giant who had supported Nanman for so many years looked pitifully small at that moment, like a child’s.

“When I faced Baeksang for the last time, do you know what I was thinking?”

I could guess well enough. But I didn’t say it.

The person who knew him better than anyone—and had suffered the most because of him—was standing right in front of me.

“I wanted to save him somehow.”

“……”

“Even in that horrific scene, I wanted to save that bastard Baeksang, who had betrayed everyone in this land, myself included, and help him run far away.”

Though they shared no blood, they were sworn brothers no different from actual family.

The Beast Miao King must have wanted to save Baeksang at any cost.

He must have wanted to absolve the man who had served as Dark Heaven’s hunting dog while his child—the child he had believed dead—was held hostage.

But the one who refused that absolution was Baeksang himself.

“He probably knew, too. That I was hesitating. That must be why he made that choice.”

The Beast Miao King’s muttering faded into the empty air.

The emotion in his voice was grief over being forced to end the life of his sworn younger brother—the man he had cherished more than his own life—with his own hands. It was also self-reproach for abandoning his duty as Palace Lord because of his personal feelings.

“One diseased tree caused the forest to die. Yet the forest keeper is now pacing in front of the diseased tree that has already fallen. Could you call such a person a forest keeper?”

I had been listening quietly to the Beast Miao King’s story. Then I broke the long silence.

“Great Hero Yayul, I’m asking this completely seriously…”

My voice faltered despite myself.

To be honest, I wasn’t even sure whether I should say this now. But somehow, I had to get that mentally shattered forest keeper back on his feet.

Even if it meant crossing the line a little—or perhaps a lot.

“Are you fucking stupid?”

“……!”

Unmistakable agitation came from the Beast Miao King’s back. But since I had already taken the first step, I continued without hesitation.

“What, is the Palace Lord some kind of god of heaven and earth? Don’t you have human emotions?”

“You…”

“Let’s be honest. Someone who spent their entire life with you, someone like family, just died. Who in this world could be fine after that? Are you supposed to be sadder just because other people died, too?”

The Beast Miao King fell silent for a moment beneath the barrage of blunt words before opening his mouth.

“Jin Taekyung, you as well?”

I nodded.

“Isn’t that only natural? What makes a bastard like me so special?”

“……”

“People around me can praise me as a chivalrous hero or a Great Hero, but I’m still a person in the end. Why would a Palace Lord be any different?”

His answer came without the slightest hesitation, and the broad back shifted.

*Rustle.*

His head slowly turned.

It was the first time I had seen the Beast Miao King’s face since entering the old shrine, and he looked utterly haggard.

“They were also Nanman people I had to protect.”

“And you protected them. Even after being branded a traitor, you came back despite the danger. It was thanks to you that countless others could be saved.”

I continued quietly.

“The diseased trees have already fallen, and the forest is still alive. If anything, it needs its forest keeper more than ever.”

Many people had been sacrificed in this incident. But ironically, Nanman would grow even stronger.

Because Baeksang had not been the only diseased tree in the vast forest called Nanman.

*The other chieftains. No—the traitors.*

Baeksang had joined hands with Dark Heaven for his child’s sake. They had followed Baeksang solely for their own safety and power.

They were the trees that should have been cut down long ago. Trees diseased with greed.

More than twenty chieftains had swayed the branches growing from their bodies while drunk on greed. Countless leaves had tumbled across a river of blood as a result, but the forest had not died.

No. Beneath a single banner called the Nanman Beast Palace, it would become more united and flourish more than ever.

And there was only one person who could raise that banner before all the people of Nanman.

“Let’s go back now. Wouldn’t it let that father and son rest easier, too?”

My voice was directed at the Beast Miao King, but my eyes were looking somewhere else.

The Beast Miao King noticed where my gaze had settled and asked quietly,

“You knew?”

“I noticed it as soon as I came in. Everything else in the shrine is covered in dust, but those are completely clean.”

I slowly walked forward.

Between the faded murals and dozens of stone statues whose identities I couldn’t determine, two memorial tablets had been placed—two that hadn’t been there the last time.

Neither tablet had a name carved into it.

But I already knew who they belonged to.

*Baeksang. Baekhwi.*

I murmured those names silently, names that even the person who had made the tablets by hand couldn’t bring himself to carve into them. Then I bowed.

Once.

And again.

When I turned around after completing the two bows, the Beast Miao King’s rigid face was waiting for me.

“Why are you looking at me like that?”

“Because it was unexpected.”

“What? Did you think I was going to knock over the tablets?”

“You could have. Especially considering the crimes committed by Baeksang.”

*Damn it. He wasn’t wrong.*

Given everything that had happened, even if I split Baeksang’s tablet in half and spat on it, it would count as self-defense.

But…

“I just… felt like doing this. That’s all.”

What was this filthy, bitter feeling?

I turned my head to look at the tablets again. And suddenly, I thought I understood what I was feeling.

Maybe it was something that should be called sympathy or empathy.

*I’m too late. I walked down a path I can never turn back from, and I will never stop.*

The voice I had heard in the dark underground prison seemed to ring faintly in my ears.

Looking at the tablet without even a single letter carved into it, I asked a question that would never be heard.

*If I had been you, what path would I have taken?*

No answer came from anywhere.

Not even from the depths of my own heart, rather than from the tablet.

Still, a thought suddenly occurred to me.

*If there really is such a thing as an afterlife, I hope that bastard—someone I could tear to pieces without feeling satisfied—gets to live an ordinary life unlike this one.*

*I hope he can spend a peaceful life without losing anyone or sacrificing anyone, together with the child he missed so terribly.*

*Damn it. How many people died because of him?*

I knew that much. There was no villain in this world without a story.

But the reason I felt so filthy was simple.

Maybe I could have walked the same path as Baeksang.

I could sufficiently imagine how desperately he had struggled within the circumstances he had been given.

That was why this was all I could say.

“Don’t commit any sins over there, you goddamn bastard.”

At that moment, reddish light streamed through the gap in the shrine door and illuminated the two tablets.

As if it meant to serve as an answer in their place.

Then, the next moment, a deep voice pierced my ears.

“The sun is already setting.”

*Cre-eak.*

The old floorboards screamed. At last, the giant unfolded his crossed legs and rose from his seat, staring at me with calm eyes.

“If we head straight to the Inner Palace now, we should still be able to have dinner together.”

“……!”

“Let’s go. We need to get back before it gets any later.”

I looked at the Beast Miao King, let out a quiet laugh, and nodded.

Nanman’s forest keeper had returned.

* * *

Two days passed.

When the Palace Lord, who had disappeared without a word, returned, the leadership—which had been thrown into confusion—quickly regained its stability. After taking a short rest at everyone’s urging, the Beast Miao King summoned me the following day.

No, to be precise, he summoned Jeok Cheongang and me.

Jeok Cheongang arrived at the meeting room hastily thrown together over seven days and nights. The moment he saw the Beast Miao King sitting there, he said,

“Our Miao King has grown up so much. He’s even sitting in the chief seat.”

“……Oh. I’m sorry. I did it out of habit.”

“No, no. I understand completely. So understand this old man’s habit of sending a Flame Divine Palm at any rude punk he sees.”

*Whoosh!*

The Beast Miao King had already experienced that habit during the Great Faction War.

He quickly moved his heavily bandaged body to vacate the chief seat, then politely gestured toward it.

“Please sit, Old Master Jeok.”

“Oh, it’s fine. You’re still injured—there’s no need to go this far.”

“……”

“Enough. Sit down already. I don’t like some wet-behind-the-ears punk ordering me around, but for now, go ahead and spout whatever you want.”

The Beast Miao King seemed confused by the gangster-like way of speaking he hadn’t heard in a long time, so I opened my mouth politely.

“You can just speak. That means he’s willing to listen.”

“……Then, Old Master Jeok, may this junior say something?”

“He really hates being asked questions in return. You’re still not fully recovered, so if you don’t want to suffer something nasty, speak right away.”

“……Understood.”

Unlike the Jeok Cheongang in his memories, the one sitting before him looked much younger. The Beast Miao King glanced at him before carefully opening his mouth.

“I asked you to join us, Old Master Jeok, because I wished to consult you about a grave matter.”

“A grave matter?”

“Yes.”

“From what I’ve heard, the aftermath has been handled smoothly so far. Did you perhaps manage to pick up Dark Heaven’s trail?”

“I wish that were the case, but unfortunately, it isn’t. In another sense, however, it is a problem even more troublesome than that…”

“You’re taking too long to get to the point. Tell me the important part before I shorten your lifespan.”

*This man really hasn’t changed.*

The Beast Miao King looked at Jeok Cheongang with exactly that thought in his eyes, then took something from inside his robes and placed it on the table.

*Thud.*

It was something wrapped in thick cloth. But everyone in the room, myself included, could sense the ominous energy seeping out from within.

As the air suddenly grew heavy, Jeok Cheongang muttered as though groaning.

“……Demonic qi?”

The Beast Miao King nodded with a grim face.

“That’s right. Very pure and powerful demonic qi at that. I couldn’t entrust it to anyone else in Nanman, so I carried it myself.”

Their voices seemed distant, like echoes.

I had a feeling I knew where this demonic qi had come from, as well as what was hidden beneath the cloth.

At the same time, the final roar of an existence that had once echoed through the deep darkness rang in my ears.

“It’s the sacred stone. The one carried by the guardian spirit.”

“As you guessed. Though it is no longer a sacred stone.”

*Rustle.*

The Beast Miao King answered in a troubled voice and peeled back the cloth. Instead of warm, dazzling radiance, a stone filled with murky darkness was revealed.

It had absorbed all the demonic qi flowing from the rift. Now, it was something that ought to be called a demonic stone, and the Beast Miao King’s gaze sank deeply as he looked at it.

“For now, I am suppressing the demonic qi. But I cannot leave it like this forever. That is why I summoned you and Old Master Jeok to discuss what should be done with it.”

At that moment—

*Ding.*

A clear chime, completely at odds with the murky darkness before me, rang out as a holographic window appeared in midair.

> **System**
>
> **Quest:** Corrupted Divine Artifact
>
> Will you accept?
>
> **Y / N**
```
