<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0663.txt",
      "sha256": "d77393e4a798955e8e752677583bf33d68f5991763dc3d40d982486eac7a0afa",
      "bytes": 13170
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e1bbd7474a187134610da78d8659ef06bdb49ed1f0d54898d842ea95304cb35a",
      "bytes": 2715
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1853e3a7a00e8b20e3049768bf03cfec3b2f3b0009c510da8dc860ee5672dc6d",
      "bytes": 201600
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "6e32ad6e30a9e22993ecc4c7402f4c4cdfc29cccfaada1471605d9fe8a2c4908",
      "bytes": 1158
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0cd4fc8ab1c62ee4f47552c4898a96c8cae883a3c31f501285e028d0a154b5b1",
      "bytes": 553
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "e8488571c19d7e8980efe73048799bf36a550b375d4d946a002a3f2ff4652f29",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "addf018ae561b0dae9226916a8a743f151587e22632fd54bbbc904505c8f5626",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "67f1905a7b32565d91abf0ee9ea991b1f379abd60618619c27faf47161bcdca2",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "9c2411b515ab5abccc74f89672d8f39ef721554705c0d5beae18addd4fbbabff",
      "bytes": 576
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "1986dc3d549dbd8c7749bfb360f203e61cea5d46b54c3de778e4ffeba4122096",
      "bytes": 585
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4b87566b04466cdedd5a25cae0dece9f1c7e71396058292555cc479cd398e2e7",
      "bytes": 206682
    }
  ],
  "estimated_tokens": 10865
}
-->

# Durable State Update — Chapter 663

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 663. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 663. Profile updates may replace only one
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
  "chapter": 663,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 663,
    "continuity_sources": [663],
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
    "Jin Taekyung remains imprisoned in the Nanman Beast Palace's underground prison, bound by iron balls and unable to use internal energy because of the Force-Sealing Pill; his execution is scheduled for noon in two days.",
    "Baeksang has secured the support of twenty tribal chieftains and is using Jin's execution as the final-day agenda of the Tribal Grand Council.",
    "Baekhwi was Baeksang's only child and was killed without leaving a corpse during the Great Snow Mountain battle; Baeksang identifies the Great Snow Fiend as the killer.",
    "Venerable Wusang was the former Sect Leader of the Zhongnan Sect, master of the Wind-and-Cloud Sword Lord, and a Supreme Peak master who died during the Great Snow Mountain battle.",
    "Baeksang claims that the Zhongnan Sect and other Western Army allies deliberately withheld support, killed the messenger, pursued retreating enemies for military credit, and erased the surviving evidence.",
    "Baeksang believes the Central Plains and Han Chinese betrayed Nanman after Nanman forces fought alongside them in the Great Faction War.",
    "Baeksang attacked Jin in the prison with tangible internal energy, injuring his forehead, while Jin remained still and confronted him.",
    "The Fire Dragon Pavilion was attacked after Jin left, Dark Heaven is suspected of involvement, and Heugung and Yohi remain missing after the destruction of Yohi's Western Yao Estate.",
    "Chief Jang and Chief Go are keeping the three Han Chinese reconnaissance-squad captives away from the Inner Palace.",
    "Song Ilseom and Hyuk Mujin remain bound and unconscious, while Ju Hwaran remains among the captives.",
    "The reconnaissance squad is traveling through Nanman while guarding against the Blood Monk."
  ],
  "continuity_sources": [
    662,
    661
  ],
  "open_questions": [
    "Whether Baeksang's account of the Western Army's betrayal and the destruction of its evidence is fully accurate remains unresolved.",
    "What did Baeksang mean when he said that Jin's people showed him what he had to do?",
    "Why did the Southern Heaven Demon Empress order or permit Jin's execution to be delayed for two days?",
    "Can Jin survive the scheduled public execution?",
    "What role did Baeksang play in the attacks and the alleged collusion with Dark Heaven?"
  ],
  "safe_through": 662,
  "temporary_decisions": [
    "Use Venerable Wusang for 무상진인.",
    "Use Great Snow Fiend for 대설귀.",
    "Use Western Army for 서군 and Southern Army for 남군.",
    "Retain Force-Sealing Pill for 금력단 and iron balls for 철구.",
    "Retain Outer Lands for 새외 and Han Chinese for 한족."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 상태               | **Status**                     |
| 길드      | **Guild**             |
| 태원     | **Taiyuan**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 서요부 | **Western Yao Estate** | Yohi's residence in the western part of the Inner Palace. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 김화종 | younger_ally_to_older_butler | Butler Kim | respectful and formal | Asks about Kim Hwajong before entering the morgue and later bids him farewell. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 662
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and joined forces with twenty tribal chieftains to arrange Jin's execution at noon in two days.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother and enduring grief, hatred, and betrayal over Baekhwi's death.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; he opposes the Nanman Beast Palace joining the Murim Alliance, distrusts the Central Plains because of the alleged wartime betrayal, and is alleged by Heugung to have colluded with Dark Heaven.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 662
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 612
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong served Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 661
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled for noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 613
- **Aliases:** Butler Kim
- **Role:** The deceased old butler who served Choi Minwoo's family and was Choi's grandfather.
- **Personality:** He showed enduring care for Choi Minwoo through the affectionate message he left at his grave.
- **Voice:** His living voice is not heard, but his written farewell is affectionate and encouraging.
- **Relationships:** Kim Hwajong was Choi Minwoo's grandfather and former butler; Choi mourns him at his grave.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 658
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃663화



“그날, 너희가 알려 주었다. 내가 어떤 길을 가야 하는지.”

씹어뱉는 듯한 목소리와 함께 짧지도, 길지도 않았던 이야기가 끝났다. 나는 차갑게 빛나는 백상의 눈동자를 말없이 응시했다.

그에게 하고 싶은 말?

글쎄. 잘 모르겠다.

눈부시도록 흰 백의(白衣)를 입은 채 내 앞에 서 있는 이 사람은, 감히 짐작할 수 없는 어둠 속에서 살아온 자다.

대의(大義)를 위해 싸웠으나 끝내 배신당했고, 목숨보다 아꼈던 자식을 잃어야 했으니까.

그가 지금껏 살아왔던 이유는 오직 한 가지뿐일 것이다.

‘복수.’

백상의 말은 틀리지 않았다. 하나뿐인 자식을 잃고 칠흑 같은 어둠 속에서 헤매던 그에게 중원인들은 냉혹한 배신으로 횃불을 비춰 주었고, 그렇게 백상은 자신 앞에 놓인 유일한 길을 발견했다.

바로 복수의 길이다.

그는 고통과 분노의 가시밭길을 걸어 이곳까지 왔고, 나는 그런 백상의 모습에서 문득 기억 속에 존재하는 누군가를 떠올렸다.

“……대장로.”

반사적으로 흘러나온 중얼거림을 들은 백상의 눈빛에 의문이 스친다. 쓰게 입맛을 다신 내가 말을 이었다.

“별거 아니야. 그냥 당신을 보고 있자니 전에 알던 사람이 떠올라서.”

“무슨 연유에서지?”

“그 사람도 당신처럼 병신 같았거든. 암천에 조종당하는 꼭두각시였지.”

“뭐?”

“하지만 한편으로는 충분히 이해할 수 있었어. 그에게도 그럴 만한 이유가 있었으니까.”

“……배신당했군.”

“그래. 그것도 자신과 같은 피가 이어진 혈육에게.”

나를 말 없이 내려다보던 백상이 입술을 뗐다.

“그는 어떻게 되었느냐.”

“죽였다. 내가 직접.”

“……!”

“가문의 큰 어른이었지만 어쩔 수 없었어. 이미 모든 게 너무 멀리 와 버렸으니까.”

“나를 비난하고 싶으냐?”

나는 피식 웃었다.

비난이라. 이제 와서 비난한다고 한들 뭐가 달라질까.

“말뿐인 비난은 아무런 효과도 없어. 그 정도로는 멈추지 못하지. 그게 대장로의 숨통을 끊은 가장 큰 이유였고.”

그것이 복수귀(復讐鬼)의 최후다.

그들은 자신들이 원치 않은 길로 들어섰다가, 영영 길을 잃어버린다. 오직 복수라는 횃불 하나만을 바라보고 달려드는 부나방과 같다.

“대장로를 죽인 뒤에 문득 그런 생각이 들더라고. 만약 그 전투에서 패배한 것이 나와 태원진가였다면…… 복수에 성공한 그는 마침내 행복해졌을까.”

“그건…….”

“아마 아니었겠지. 그는 오로지 복수를 위해 살아왔지만, 어느 순간 그 분노는 무뎌졌고 죄 없는 사람들이 희생당하는 모습을 보며 죄책감을 품었을 테니까.”

나는 대답을 기다리지 않고 말을 이었다.

“바로 지금의 당신처럼.”

“……!”

일그러진 백상의 얼굴을, 나는 담담하게 응시했다.

“난 분명히 당신을 이해하지 못한다. 당신과 같은 일을 겪지 못했고, 수십 년 동안이나 복수심에 불탄 적도 없으니까. 하지만 한편으로는 인정해. 적어도 내게 있어 중원인들과 한족을 향한 당신의 분노는 정당하다.”

“……정당하다고?”

백상이 굳은 얼굴로 되묻는다. 아마 그로서도 예상치 못한 대답이었겠지만, 조금 전 내가 했던 말은 모두 진심이었다.

물론 지금 입 밖으로 흘러나오는 말 역시도.

“그래. 나 같아도 그랬을 거야. 아니, 내가 당신이었다면 이미 중원 전체가 내 적이었을지도 모르지.”

문득 아레스 길드로 향하던 그 날이 떠오른다.

그때의 나는 혼자였지만, 내딛는 걸음에는 한 치의 망설임도 없었다.

하지만 그런 선택을 한 것은 내게 충분한 힘이 있었기 때문이 아니다. 김화종의 죽음에 진심으로 분노했기 때문이었다.

그렇게 나는 아레스 길드를 무너트렸다.

진태경이 아니라 백상이었다면, 중원을 무너트리기 위해 싸웠을 거다.

하지만…….

“당신의 그 분노가, 이 땅에 살아가는 남만인들에게도 정당할까?”

“……!”

“물론 이해하는 사람도 있겠지. 하지만 당신이 암천과 결탁하는 과정에서 생겨난 희생자들은 무슨 죄지? 그들의 가족은? 연인과 친구는?”

백상의 전신이 덜컥 흔들린다. 나는 담담한 목소리로 계속해서 말을 이었다.

“처음 남만에 발을 디뎠을 때 어떤 소식을 들었지. 한족 무리에 의해 묘족 마을 하나가 몰살당했다는. 남녀노소 가릴 것 없이 백명을 학살한 한족들도 결국 독에 의해 양패구상했어.”

적막한 뇌옥에 홀로 갇혀 있다는 것은, 생각할 시간이 많다는 뜻이기도 하다.

나는 처음부터 지금까지의 일을 되짚으며 확신할 수 있었다.

“아무리 생각해도 희한한 일이지. 아무리 전투가 벌어졌다지만, 그 많은 사람들 중에 살아남은 이가 하나도 없다는 건.”

그건 처음부터 계획된 흉계(凶計)였다.

묘족 마을 하나를 지워 버림으로써, 남만 땅 전체에 한족에 대한 적개심이 끓어오르게 만든 것이다.

“그뿐만이 아니야. 갑작스럽게 독혈지를 벗어난 천년지주들과 이번 서요부에서의 일도 있지. 묘족 마을까지 더한다면 죽은 이들의 숫자만 족히 삼백여 명이다.”

이것이 내가 남만야수궁에 오고 난 후 고작 칠주야(七晝夜) 만에 벌어진 일이다.

백상이 복수귀로 살아온 지난 수십여 년에 비하면 한 줌밖에 안 되는 시간. 그리고 그보다 더 무서운 것은, 앞으로의 일이었다.

그가 완전한 복수를 완성하기 위해서는, 중원과의 전쟁은 우연이 아닌 필연이니까.

“도대체…….”

나는 안타까움과 분노를 담아 백상을 바라보았다.

“앞으로 얼마나 더 많은 피를 흘릴 셈이냐, 백상.”



* * *



철벅. 철벅.

나아가는 한 걸음, 한 걸음마다 오랜 시간 뇌옥 바닥에 고여 있던 구정물이 사방으로 튀었다.

그러나 걸음의 주인은 눈처럼 새하얀 옷자락이 더럽혀지는 것을 신경 쓰지 않았다.

아니, 뇌리를 가득 채운 어떤 생각으로 인하여 눈치채지 못했다고 하는 것이 옳았다.

철벅…….

이미 흠뻑 젖어 버린 가죽신이 불현듯 움직임을 멈춘다.

홀로 뇌옥을 가로지르던 중년인, 백상은 문득 자신의 어깨너머를 돌아보았다.

어둡고, 차갑고, 적막하다.

마치 자신이 걸어온 길처럼. 그리고 저 너머에 갇혀 있는 한 사람이 앞으로 걸어가야 할 길처럼.

하지만 그는, 진태경은 자신과 같은 길을 걷지 못할 것이다.

공개 처형까지 남은 시간은 고작 이틀.

장장 수십여 년의 세월을 걸어온 백상과 달리 진태경에게 남은 길은 너무나도 짧고 분명했으니까.

‘이미 끝난 것이나 다름없다. 놈은 빠져나오지 못해.’

진태경의 무위가 어느 정도인지는 이미 알고 있다.

온갖 명문대파가 산재한 중원에서도 단연 두각을 드러내고 있는 초절정 고수.

비록 백상 역시 전력을 다한 것은 아니었지만, 며칠 전 짧게 수를 주고받은 순간 본능적으로 알아차릴 수 있었다.

자신보다 반 수. 아니, 어쩌면 한 수 위.

진태경은 상상을 뛰어넘는 괴물이었다. 그러나 공력이 금제(禁制)되고, 엄청난 무게의 철구로 구속되어 있는 상태라면 설령 그의 스승인 화왕이 온다 해도 살아남을 수 없다.

더군다나 놈에게는 철구보다 더욱 큰 구속이 존재했다.

‘휘하의 한족들.’

진태경은 자기 사람을 아낀다. 그렇기에 도주하는 대신 스스로 투항하여 뇌옥에 갇히는 것을 선택했다.

참으로 멍청하게도.

백상이 바라본 저 괴물 같은 청년의 가장 큰 약점은, 바로 인정(人情)이었다.

그 어떤 것보다 무림인을 무림인답지 않게 만드는 것.

하지만…… 무엇보다 사람을 사람답게 만드는 것.

그리고 눈으로 뒤덮인 대설산이 피로 물들던 그 날. 백상이 아군에게 간절히 원했던 그것.

‘그러고 보니. 그때의 휘아도 저 나이쯤이었지.’

백상은 공허한 눈으로 허공을 바라보았다. 어둠만이 존재하는 허공에 한 사람의 얼굴이 스쳐 지나간다.

갓난아이에서 소년으로, 소년에서 청년으로.

누구보다 올곧았고, 휘(輝)라는 이름만큼이나 밝게 빛났던 자신의 하나뿐인 자식을.

그리고 두 번 다시 보지 못할 그 아이의 웃는 얼굴을.

꾸국.

자신도 모르는 사이에 한껏 움켜쥔 주먹. 가지런히 정돈된 손톱이 살점을 파고들자 핏물이 흘러나온다.

툭, 투둑.

백상의 시선이 발아래를 향했다. 고여 있는 구정물 위로 퍼져 가는 붉은 핏방울이 보였다.

그럴 때마다 일어나는 작은 파문이 한 사람의 얼굴을 그려 냈다.



‘앞으로 얼마나 더 많은 피를 흘릴 셈이냐, 백상.’



계속해서 귓가에 맴도는 진태경의 마지막 한 마디. 하지만 백상의 대답은 그때도, 지금도 같았다.



‘나는 이미 강을 건넜다. 두 번 다시 돌아갈 수 없는 강을.’



그가 강을 건넌 것은 오래전의 일이다.

절망과 분노에 의해 반쯤 미쳐 가던 백상은 어느 날 정체를 알 수 없는 아름다운 여인을 만났고, 그녀의 외모보다 더욱 매혹적인 제안을 받았다.

아니, 거절할 수 없는 제안을.



‘선택하세요. 하면 반드시 이루어질 테니.’



백상은 망설이지 않았다.

삶의 목표가 생긴 그는 여인이 내민 손을 기꺼이 맞잡았고, 지금껏 단 한 번도 그 결정을 후회하지 않았다.

아니, 후회해서는 안 됐다.

‘하지만 어째서…….’

지난 수십여 년의 결실을 코앞에 둔 지금, 왜 자신은 흔들리고 있는가.

백상은 새어 나오려는 목소리를 삼키며 이를 악물었다. 그리고 이미 더럽혀진 가죽신과 더 이상 백의(白衣)라 부를 수 없는 자신의 옷자락을 바라보며 되뇌었다.

‘이틀 뒤. 모든 것이 끝난다. 모든 것이.’

백상의 발아래, 고여 있는 구정물 위로 핏방울이 번진다.

이미 오래전부터 더럽혀진 그것은 피를 머금어 서서히 붉어지고 있었다.

그가 지금껏 걸어왔던 길처럼. 앞으로 걸어갈 길처럼.

철벅.

거칠게 웅덩이를 짓밟은 백상은 멈췄던 걸음을 옮기기 시작했다.

누구도 입을 열지 않는 적막한 공간 속, 여전히 귓가에 메아리치는 진태경의 목소리를 들으며.



* * *



백상이 떠났고, 나는 다시 홀로 남았다.

팽팽하게 당겨진 쇠사슬과 만근의 철구에 구속되어 있는 전신은 뻣뻣하게 굳어 가는 중이었다.

‘음. 젠장.’

막상 백상이 떠나고 나니까 좀 아쉽다.

차라리 살려 달라고 빌 걸 그랬나, 싶기도 하지만 그래도 후회는 없다. 할 말도 충분히 했고.

추하게 목숨을 구걸해 봤자 남는 것도 없었다.

백상은 오직 복수 하나만을 바라보고 살아온 사람이다. 내가 애걸복걸한다고 해서 휴먼 다큐 본 아주머니처럼 눈물 글썽거릴 일 따위는 없다.

물론 그렇다고 해서, 이틀 뒤 끌려 나가 얌전히 죽음을 맞이할 생각도 없다.

‘미쳤나. 어떻게든 살아야지.’

백상의 분노를 인정한다고 했던 건 사실이다.

하지만 그게 내가 놈에게 죽을 만한 이유가 되지는 않는다. 내 시선에는 대장로도, 백상도 사연 있는 병신들일 뿐이었다.

그리고 난 이역만리 타지까지 찾아와서 만난 저 새로운 병신을, 어떻게든 막을 생각이었다.

‘그런데 어떻게 빠져나가지?’

말도 많이 하고, 생각도 많이 했더니 목이 탄다.

내가 마른침만 꼴깍 삼키고 있던 그때, 위에서 차가운 무언가가 정수리에 닿았다.

툭.

“어?”

물이다. 비록 퀴퀴하고 맛도 없겠지만, 물이라는 게 중요하다. 아마 백상이 주위를 박살 낼 때 천장이 더 벌어진 모양이었다.

‘이건 도움이 되네.’

내심 중얼거린 나는, 천장을 향해 고개를 젖혔다.

그리고 다음 순간, 갈라진 천장 틈새 사이로 예상치도 못했던 누군가의 눈동자와 시선이 닿았다.

송아지처럼 커다랗고 투명한 눈.

“……너, 왜 거기 있냐?”

눈의 주인이 대답했다.

“태산이. 배고프다. 밥 너무 먹는다고 뇌옥에 갇혔다.”

“아.”

그럼 인정이지.
```

## Final English reading copy

```markdown
# Chapter 663

“That day, you people showed me which path I should take.”

With those words spat out in a bitter voice, his story—neither short nor long—came to an end. I silently stared into Baeksang’s coldly gleaming eyes.

What did I want to say to him?

*Well… I don’t know.*

This man standing before me in dazzlingly white robes had lived through a darkness I could not even begin to imagine.

He had fought for a righteous cause, only to be betrayed in the end. He had lost the child he cherished more than his own life.

There could only be one reason he had continued living all this time.

*Revenge.*

Baeksang wasn’t wrong. After losing his only child and wandering through pitch-black darkness, he had been shown a torch by the cold betrayal of the Central Plains people. And with that light, Baeksang had discovered the only path laid out before him.

The path of revenge.

He had walked a thorny road of pain and fury to reach this place, and seeing him suddenly reminded me of someone else from my memories.

“…The Head Elder.”

A flicker of confusion crossed Baeksang’s eyes when he heard the mutter that escaped me before I could stop it. I bitterly smacked my lips and continued.

“It’s nothing. Looking at you just reminded me of someone I used to know.”

“For what reason?”

“He was an idiot, too. Just like you. A puppet controlled by Dark Heaven.”

“What?”

“But at the same time, I could understand him well enough. He had his reasons.”

“…He was betrayed.”

“Yeah. By someone who shared his own blood.”

Baeksang silently looked down at me before parting his lips.

“What became of him?”

“I killed him. With my own hands.”

“…!”

“He was one of the senior figures in my family, but I had no choice. Things had already gone too far.”

“Do you wish to condemn me?”

I let out a short laugh.

Condemn him? What would condemning him accomplish now?

“Condemnation that ends with words has no effect. Someone like that won’t stop over something so trivial. That was the biggest reason I cut the Head Elder’s life short.”

That was how revenge fiends met their end.

They stepped onto a path they had never wanted to take, then lost their way forever. They were like moths rushing toward a single torch—the torch of revenge.

“After killing the Head Elder, I suddenly had a thought. If I and the Jin Family of Taiyuan had been the ones to lose that battle… after succeeding in his revenge, would he finally have become happy?”

“That…”

“Probably not. He lived only for revenge, but at some point, his anger must have dulled, and watching innocent people be sacrificed must have left him feeling guilty.”

I continued without waiting for an answer.

“Just like you do now.”

“…!”

I calmly looked into Baeksang’s twisted face.

“I definitely don’t understand you. I’ve never gone through what you did, and I’ve never burned with revenge for decades. But at the same time, I admit it. At least as far as I’m concerned, your anger toward the Central Plains people and the Han Chinese is justified.”

“Justified?”

Baeksang asked again with a rigid expression. It was probably an answer he had not expected, but everything I had said a moment ago had been sincere.

And so were the words leaving my mouth now.

“Yeah. I would’ve done the same thing if I were you. No—if I had been in your place, perhaps the entire Central Plains would already have been my enemy.”

Suddenly, I remembered the day I had headed for the Ares Guild.

Back then, I had been alone, but there had not been even a trace of hesitation in my steps.

It wasn’t because I had possessed enough strength to make that choice. It was because I had been genuinely furious over Kim Hwajong’s death.

That was how I brought down the Ares Guild.

If I had been Baeksang instead of Jin Taekyung, I would have fought to bring down the Central Plains.

But…

“Is that anger of yours justified toward the Nanman people living on this land, too?”

“…!”

“Of course, there must be people who understand you. But what crime did the victims created by your alliance with Dark Heaven commit? What about their families? Their lovers and friends?”

Baeksang’s entire body jerked. I continued in a calm voice.

“When I first set foot in Nanman, I heard some news. A Miao village had been massacred by a group of Han Chinese. Those Han Chinese had slaughtered a hundred people, men, women, and children alike, but in the end, both sides had been destroyed by poison.”

Being locked alone inside an underground prison meant having a great deal of time to think.

As I went over everything that had happened from beginning to end, I could reach only one conclusion.

“It’s strange, no matter how I think about it. Even if a battle had taken place, how could there not have been a single survivor among all those people?”

It had been a sinister plot planned from the very beginning.

By wiping out a single Miao village, they had caused hostility toward the Han Chinese to boil across all of Nanman.

“And that isn’t all. The Thousand-Year Spiders that suddenly escaped the Poisonblood Grounds, and what happened at the Western Yao Estate. Add the Miao village to that, and the number of dead easily exceeds three hundred.”

All of that had happened in a mere seven days and nights since I arrived at the Nanman Beast Palace.

Compared to the several decades Baeksang had spent living as a revenge fiend, it was barely a moment. And what frightened me even more was what lay ahead.

For him to complete his revenge, a war with the Central Plains was not a possibility born of chance.

It was inevitable.

“Just how…”

I looked at Baeksang with pity and anger.

“How much more blood do you intend to spill, Baeksang?”

* * *

Splash. Splash.

With every step he took, stagnant, foul-smelling water that had been pooled on the floor of the underground prison for a long time splashed in every direction.

But the owner of those footsteps did not care that the hems of his snow-white robes were getting dirty.

No. It would be more accurate to say that he failed to notice because his mind was filled with other thoughts.

Splash…

The leather shoes, already soaked through, suddenly stopped moving.

While crossing the underground prison alone, the middle-aged man, Baeksang, suddenly looked back over his shoulder.

Dark, cold, and silent.

Just like the path he had walked.

And just like the path the one imprisoned beyond this point would have to walk from now on.

But he—Jin Taekyung—would not be able to walk the same path.

There were only two days left until the public execution.

Unlike Baeksang, who had walked for several decades, Jin Taekyung had a path that was far too short and clear.

*It is already as good as over. He will not escape.*

Baeksang already knew roughly how great Jin Taekyung’s martial prowess was.

A Supreme Peak master who stood out even in the Central Plains, where countless prestigious sects had taken root.

Though Baeksang himself had not fought at full strength, he had instinctively realized it when they had briefly exchanged moves several days earlier.

*Half a move above me. No… perhaps an entire move.*

Jin Taekyung was a monster beyond imagination. But with his internal energy sealed and his body restrained by iron balls of enormous weight, he could not survive even if his master, the Fire King, came to save him.

And there was an even greater restraint binding him than the iron balls.

*The Han Chinese under his command.*

Jin Taekyung cared about his people. That was why he had chosen to surrender and be locked inside the underground prison instead of fleeing.

*What a fool.*

The greatest weakness of that monstrous young man Baeksang had observed was his human compassion.

The very thing that made a martial artist unlike a martial artist more than anything else.

But…

More than anything, it was the thing that made a person human.

And on that day when the snow-covered Great Snow Mountain had been dyed red with blood, it was the very thing Baeksang had desperately wanted from his allies.

*Come to think of it, Hwi was about that age then, too.*

Baeksang stared blankly into the empty air. In the darkness where nothing existed, a face briefly passed through his mind.

From an infant to a boy, and from a boy to a young man.

His only child, who had been more upright than anyone and shone as brightly as his name, Hwi.[^1]

And the smiling face of the child he would never see again.

Crunch.

Without realizing it, Baeksang clenched his fist tightly. His neatly trimmed nails dug into his flesh, and blood began to flow.

Drip. Drip-drip.

Baeksang lowered his gaze toward his feet. He saw red drops of blood spreading across the stagnant water.

Each small ripple that formed drew the outline of one person’s face.

*How much more blood do you intend to spill, Baeksang?*

Jin Taekyung’s final words continued to echo in his ears.

But Baeksang’s answer had been the same then as it was now.

*I have already crossed the river. I can never go back.*

He had crossed that river a long time ago.

Baeksang had been half-mad with despair and rage when he met a beautiful woman whose identity he could not discern one day. She offered him something even more captivating than her appearance.

No.

She offered him something he could not refuse.

*Choose. If you do it, it will definitely come to pass.*

Baeksang had not hesitated.

Once he had found a goal in life, he had gladly taken the hand she held out to him, and he had never regretted that decision.

No.

He must not regret it.

*But why…?*

Now that he was standing on the verge of finally reaping the fruits of several decades, why was he wavering?

Baeksang swallowed the voice trying to escape him and clenched his teeth. Then, as he looked at his already filthy leather shoes and the hems of his robes that could no longer be called white, he repeated the words to himself.

*In two days. Everything ends. Everything.*

At Baeksang’s feet, drops of blood spread across the stagnant water.

The water had been dirty for a long time already, and as it absorbed the blood, it slowly turned red.

Just like the path he had walked.

Just like the path he would walk from now on.

Splash.

Baeksang roughly stomped through the puddle and began walking again.

In the silent space where no one opened their mouth, he listened to Jin Taekyung’s voice still echoing in his ears.

* * *

Baeksang had left, and I was alone again.

My entire body, restrained by tightly drawn chains and iron balls weighing ten thousand geun, was gradually growing stiff.

*Damn.*

Now that Baeksang was gone, I felt a little disappointed.

Maybe I should have begged him to spare me. But even so, I didn’t regret it. I had said everything I needed to say.

There was nothing to gain from begging for my life in such an ugly manner.

Baeksang had lived while looking at nothing but revenge. Even if I begged and pleaded, he wasn’t going to tear up like some middle-aged woman who had just watched a human-interest documentary.

Of course, that didn’t mean I intended to be dragged out two days from now and quietly accept my death.

*Are you crazy? I have to survive somehow.*

It was true that I acknowledged Baeksang’s anger.

But that didn’t make it a good enough reason for him to kill me. From my perspective, both the Head Elder and Baeksang were just idiots with sad stories.

And I intended to stop this new idiot I had met after traveling all the way to a foreign land, no matter what it took.

*But how do I get out?*

After talking so much and thinking so much, my throat was parched.

I was swallowing dryly when something cold touched the crown of my head from above.

Tap.

“Huh?”

It was water. It might have been stale and tasteless, but the important thing was that it was water. The ceiling had probably opened up farther when Baeksang smashed the surrounding walls.

*That’s useful.*

I muttered inwardly and tilted my head back toward the ceiling.

The next moment, my eyes met someone’s completely unexpected gaze through a crack in the broken ceiling.

Huge, clear eyes like a calf’s.

“…Why are you up there?”

The owner of those eyes answered.

“Taishan. Hungry. Got locked in underground prison because they said Taishan eats too much.”

“Ah.”

Then that checks out.

[^1]: *Hwi* (輝) means “shining.”
```
