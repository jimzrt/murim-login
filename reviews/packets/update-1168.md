<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1168.txt",
      "sha256": "3b73f28df53bac62fd15baa0b11b989237b41bcd76b8e8440fa90c443c47f2a3",
      "bytes": 11497
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7f36459413ebbc045b9e8deea2f415a3cf8210620ae341b77ae6cf3fbc0846e3",
      "bytes": 716
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "629c127707aeb33bfd33dddf3e4142c30166c25d518472a55ae7f7af5cf583ca",
      "bytes": 247860
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "d10e752ed71df0fe7330e4e2f02eef7171a0853538b47800808b7f9e67c3aa6d",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4812d9f61f0986b16ae92288d3d7947919a7b583aa3b804f9f48c96cb3c5ade4",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "acfc76be2e5d7f961b09e5cf72523492f68a14e24ee1fbee303445213b56c069",
      "bytes": 1642
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6d23e18ea1c13ac94dc0d7271514fd005e33e9e0a7340eadc05fbf9909ec3672",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "023d4052c3f4a0e09a2fbf3970d3a35e16614a53d243cdac0abd2a0af714dabe",
      "bytes": 841
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "8f36be4c4a157df4a6bb926a64152fbb52e596b272c544a8db0a479c62de98ba",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 8994
}
-->

# Durable State Update — Chapter 1168

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1168. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1168. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1168,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1168,
    "continuity_sources": [1168],
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
    "Jin entered No-self and acts through what he perceives without understanding his own actions.",
    "Jin deflected Morgoth’s Dragon Breath, escaped the spells and gravity surrounding him, and split the Breath with the Fire Dragon Divine Spear’s second form, Heavenly Strike.",
    "Jin’s spear struck the unhealed wound on Morgoth’s foreleg left by the Skeleton King.",
    "Magic Johnson suffered a mana backlash after Morgoth stopped his Hell Fire with Anti Magic."
  ],
  "continuity_sources": [
    1166,
    1167
  ],
  "open_questions": [
    "What is the outcome of Jin and Morgoth’s clash?"
  ],
  "safe_through": 1167,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 레벨               | **Level**                      |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1167
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1167
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1167
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he masks fear with anger and protects those he cherishes, while recognizing that his enemies fear him too.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; seven of his allies’ old S-rank Hunter comrades are Morgoth’s soul-stolen Guardians, whom the arriving Hunters now fight.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1167
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1167
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, he treats powerful beings as trophies out of possessive desire, but can recognize and accept his own fear as a reason to grow stronger.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth holds the Skeleton King as a trophy and commands seven soul-stolen S-rank Hunters as Guardians.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1167
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1168화



닿았다.

그리고 베었다.

그뿐이었다.

찰나의 순간 시작되고 끝난 그 모든 과정에 있어서, 더 이상의 설명은 필요 없었다.

처음부터 진태경의 마음에는 한 줌의 의심조차 깃들어 있지 않았고, 망설임 없이 나아간 겁화의 창날은 그 무엇이든 녹이고 갈라 낼 수 있었다.

설령 그것이, 용의 뼈와 가죽이라 할지라도.

서걱.

한 끗.

고작 그 정도 차이였다.

그러나 단검보다 짧은 그 길이의 차이가 만들어 낸 결과는, 하늘과 땅 사이의 거리만큼이나 멀고 깊었다.

화룡갑(火龍鉀)을 아슬아슬하게 스쳐 지나간 거대한 발톱과 달리, 완벽한 궤적을 그리며 솟아오른 창날은 앞발에 아로새겨진 미세한 상처를 정확히 파고들었으니.

푸화아아악!

마치 폭포수처럼 터져 나오는 핏물.

기이하리만치 은빛을 띤 용의 피는 일순간 온 시야를 뒤덮은 것으로도 모자라 지독한 산성(酸性)으로 드러난 살갗과 화룡갑의 일부를 녹이기까지 했으나, 진태경은 아랑곳하지 않았다.

아니, 그럴 이유가 없었다.

지금까지 일어난 모든 일과, 앞으로 벌어질 일에 비하면 이 정도 고통은 아무것도 아니었으니까.

으득.

희미하게 느껴지는 통증 속, 진태경은 이를 악물었다.

동시에 어느덧 발아래 놓인 드래곤의 앞발을 디딤돌로 삼아 발걸음을, 힘껏 말아쥔 일권을 뻗었다.

‘멸염신권(滅炎神拳).’

퍼어엉!

벼락처럼 내뻗은 일권(一拳)에 압축된 공기가 폭발한다.

주먹 끝에 실린 맹렬한 열기가 비산하던 핏물을 집어삼키고, 그 너머로 새로운 길이 열렸다.

쐐애애액!

그것은 질주였다.

한 인간의 모든 것을 건 질주이자, 막아서는 모든 것을 녹이고 집어삼킬 겁화의 폭풍이기도 했다.

콰드드득!

빙하를 부수며 나아가는 쇄빙선처럼 그려지는 화염의 길.

적의 살과 뼈를 깊숙이 파고든 창날이 용암을 뿜어내며 위로, 또 위로 솟아오른다.

화살처럼 쏘아지는 신형을 따라 일어나는 불길은, 지금까지도 끝없는 전투를 이어 가던 모두의 시선을 빼앗을 만큼 강렬하면서도 선명했다.

인간도, 몬스터도.

그 누구도 예외는 없었다.

그들은 자신도 모르게 손에 쥔 날붙이를 내려놓거나, 날카로운 발톱과 이빨을 숨겼다.

이 참혹한 전장에서 살아남은 모든 생명체가 본능적으로 느끼고 있었다.

공간을 살라 먹으며 솟아오르는 저 화염이, 그들 모두의 운명을 결정지으리라는 사실을.

만약 예외가 있다면, 그것은 오직 처음부터 줄곧 서로만을 마주하고 있던 두 존재뿐이었다.

이 드넓은 전장과 그들을 바라보는 무수한 시선을 뒤로한 채, 마지막 순간을 향해 치닫고 있는 한 마리의 고룡과 인간은 마치 신화 속 한 장면처럼 서로를 응시하고 있었다.

‘진태경.’

‘모르고스.’

입이 아닌 눈으로, 허공을 격하여 스쳐 지나가는 들리지 않는 속삭임.

그렇기에 들리지 않아도 들을 수 있었다.

동시에, 말하지 않아도 느낄 수 있었다.

마치 느려진 시간을 거스르듯, 바람처럼 가까워지는 적의 눈동자에 담겨 있는 감정도 함께.

그리고 지금 이 순간 진태경이 보고 있는 것은, 극심한 통증과 두려움에 휩싸인 드래곤의 두 눈동자였다.

‘그래, 고통스럽겠지.’

닿지 않을 마음속 뇌까림과 함께, 진태경은 더욱 힘을 실어 신형을 내쏘았다.

길고도 거대한 모르고스의 앞발을 계단 삼아, 마천루(摩天樓)처럼 우뚝 솟아 있는 머리를 향해 내달렸다.

‘네 손으로 죽인, 혹은 너로 인해 소중한 누군가를 잃었던 사람들처럼.’

진태경은 문득 생각했다.

바로 지금 울려 퍼지고 있는 모르고스의 고통 어린 울부짖음이, 놈이 느끼고 있을 모든 감정과 고통이 그들 모두에게 닿았으면 좋겠다고.

수천만 명이 죽었다.

수억 명이 가족을, 친구를, 터전을 잃었다.

그것이 진태경이 멈출 수 없는 이유였다.

나아가고자 하는 의지의 밑거름이었다.

콰드드드득!

아마도 그래서일 것이다.

그의 의지가 육체의 한계를 뛰어넘은 것은.

시시각각 줄어드는 하단전의 공백만큼 힘을 잃어 가던 화염의 창날이 다시금 되살아나고, 산성을 머금은 용의 핏물에 피부와 근육의 일부가 녹아내렸음에도 통증조차 느껴지지 않는 것은.

후우우우웅!

돌연 어두워지는 하늘과 함께, 양옆으로 들이닥치는 돌풍.

그러나 진태경은 조금도 동요하지 않았다.

태산을 으스러트릴 만큼 강대한 힘으로 다가오는 두 날개를 향해, 적의 몸뚱어리를 베어 가르던 창날을 그대로 쳐올릴 뿐.

스아아악.

넘실거리는 화염이 비스듬히 솟아오른다.

소름 끼치도록 쾌속하면서도 광포한 한 줄기의 선.

불현듯 허공에 그려진 그 검푸른 불길의 궤적에는, 지난 수천 년간 광활한 창공을 지배하고 대지를 뒤덮었던 용의 두 날개가 있었다.

서걱!

- 크아아아악!

먹먹한 비명과 함께 요동치는 몸뚱어리를 짓누르며, 진태경은 발끝에 힘을 실었다.

화륵, 퍼어엉!

염화일로(炎火一路).

그 명칭에 걸맞는 맹렬한 폭발을 추진력 삼아 솟구치는 신형이, 모르고스의 칠흑빛 눈동자에 비쳤다.

아니, 틀렸다.

마침내 승천의 시기를 맞이한 한 마리의 화룡처럼 하늘로 날아오른 그의 모습은, 단순히 눈에 비친 것을 넘어 넘쳐 흐르고 있었다.

- ……!

시간이 멈춘다면 이런 기분일까.

주위의 모든 소리도, 움직임도 사라진 그 기이한 감각 속에서 모르고스는 진태경을 보았다.

무저갱처럼 깊게 가라앉은 눈빛과 어디서도 본 적 없는 검푸른 안광(眼光)을, 더불어 그 안에 스며 있는 무수한 감정의 편린을 느꼈다.

한 걸음 늦게 찾아온 깨달음도 함께.

‘늦었다.’

이와 같은 결론을 내린 것이 이성인지, 본능인지는 알 수 없었으나 한 가지는 확실했다.

모든 것이 멈춰 버린 이 세상 속에서, 오직 홀로 느릿하게 떨어져 내리고 있는 저 창날은 자신이 가진 지닌 어떤 능력으로도 막을 수도 피할 수도 없으리라는 사실을.

그렇기에, 그에게 남은 길은 하나뿐이었다.

- 크아아아아!

거대한 아가리가 벌어진다.

죽음을 불사한 고룡의 마지막 몸부림과 함께, 그 안에 도사린 강대한 마력과 수많은 이빨이 한 인간을 향해 번뜩였다.

그리고 바로 그 순간.

구구국.

진태경은 남은 힘을 다해 창대를 부여잡았다.

전신의 근육이 부풀어 오르고, 수백 개의 혈도를 타고 질주한 화염이 전신의 사지 백해로 뻗어나갔다.

쿵. 쿵. 쿵.

심장이 거세게 두 방망이질 친다.

레벨 업으로 인한 한차례의 회복도 무색해질 만큼 텅 비어 버린 하단전과 이미 한계를 아득히 넘어선 정신은 줄곧 피로를 호소한다.

그러나 그는 멈추지 않았다.

정확히는, 멈출 이유가 없었다.

‘보여.’

형형색색의 선으로 물든 이 새로운 세상 속에서, 가장 선명하게 빛나고 있는 하나의 궤적.

심안(心眼)을 통해 읽어 낸 그 길을 따라, 진태경은 자신의 모든 힘과 의지를 실어 창날에 실었다.

화륵-

되돌아오는 시간 속, 창날에 실려 있던 화염이 휘청였다.

하지만 그것은 결코 위태로움이 아닌, 찰나의 순간 일어난 변화이자 진화였다.

스아아악.

흔들리던 화염이 하나로 모인다.

불꽃이 아닌 하나의 선으로, 창날 그 자체라도 된 것처럼 뭉치고 이어지더니 끝내 가라앉는다.

불이 지닌 본연의 흉포함에서 한 걸음 더 나아간, 극도로 정제된 겁화(劫火)로서.

그리고 그것은 진태경이 스스로의 깨달음을 바탕으로 쌓아 올린 봉우리이자, 그 누구도 알려 준 적 없는 세 번째 길.

화룡신창(火龍神槍).

제 삼초식(三招式).

솨아아악.

공간이 일그러진다.

하늘을 쪼갤 듯이 솟아 있던 창날이, 그 안에 정제된 화염이 끔찍한 열기를 토해 낸다.

마치, 새로운 하늘을 위해 준비된 또 하나의 태양처럼.

‘개천(開天).’

몸과 뇌리를 지배하는 강렬한 전율 속, 진태경은 들리지 않는 포효와 함께 타오르는 겁화의 창날을 내리그었다.

콰아아아아!

검푸른 태양이, 어둠에 잠겨 있던 세상을 열었다.



* * *



들었으나 듣지 못했고.

보았으나 보지 못했다.

시체의 산과 피의 강물의 틈새에서, 저 멀리 펼쳐진 믿을 수 없는 광경을 바라보던 수많은 생명체는 지금 이 순간 동일한 감정을 공유하고 있었다.

전율.

그들은 전율했다.

그 누구도 똑바로 쳐다볼 수 없을 만큼 눈부신 섬광이 시야를 뒤덮고, 먹먹한 굉음이 귀를 막았음에도 살아남은 모든 이는 선명하게 느낄 수 있었다.

길고도 참혹했던 이 거대한 전투가 마침내 막을 내렸다는 것을.

그리고 이내 서서히 사그라지는 섬광 너머로 드러난 광경은, 그들의 짐작이 사실이었음을 증명하고 있었다.

콰아아아아.

맹렬한 바람이 휘몰아친다.

은빛 핏물을 폭포수처럼 흩뿌리며 떨어져 내리는 거대한 몸뚱어리를 휘감으며.

그래, 그것은 추락이었다.

그와 동시에, 수천 년의 세월을 살아온 어느 고룡의 몰락이기도 했다.

추락하는 것에는 날개가 있고, 그의 날개는 두 번 다시 날아오를 수 없을 터이니.

콰아아아앙!

대지가 뒤흔들린다. 자욱하게 솟아오른 흙먼지가 사막의 모래 폭풍처럼 일대를 휘감는다.

그러나 이 모든 광경을 지켜보고 있던 수만 쌍의 눈동자는 아직도 하늘을 향하고 있었다.

정확히는, 세상을 짓누르고 있는 이 지독한 정적(靜的) 속에서 홀로 움직이고 있는 한 존재를.

스륵.

보이지 않는 계단이라도 있는 것처럼 허공을 밟으며 천천히 나아가는 발걸음.

멀리서 보기에도 극심한 피로에 지친 모습이었으나, 이 자리의 그 누구도 감히 그런 생각과 감정을 품지 못했다.

어느덧 먹구름이 흔적도 없이 찢겨 나간 하늘과 쏟아지는 석양을 등진 채 지상을 향해 내려오는 그의 모습은, 그 자체로 아득한 경이를 불러일으켰으니까.

마치, 인간을 초월한 다른 존재처럼.

혹은 이 세상에 영원히 기억될 어떤 이의 옛 모습처럼.

“……스카이.”

이름 모를 누군가의 입술 사이로 탄성과도 같은 혼잣말이 흘러나온 그 순간.

떨리는 시선으로 그런 진태경의 모습을 지켜보던 사람들은, 지금껏 잊고 있었던 한 가지 중요한 사실을 깨달았다.

승리했다.

그들이.

아니, 인류가.

그리고 그들을 이끈 것은, 새로운 인류의 구원자였다.
```

## Final English reading copy

```markdown
# Chapter 1168

It connected.

And it cut.

That was all.

There was no need to explain anything more about the whole process, which had begun and ended in an instant.

Not even a trace of doubt had entered Jin Taekyung’s mind from the start, and the hellfire spearhead that surged forward without hesitation could melt and cleave through anything.

Even dragon bone and hide.

*Shhk.*

A hair’s breadth.

That was all the difference.

But the result of that difference—shorter than a dagger—was as vast and deep as the distance between heaven and earth.

The enormous claw had barely grazed his Fire Dragon Armor. The spearhead that shot upward in a perfect arc, however, pierced straight into the tiny wound etched into the Dragon’s foreleg.

*Fwoooosh!*

Blood burst forth like a waterfall.

The Dragon’s blood, strangely tinged with silver, flooded his vision in an instant. Its vicious acidity even began to melt Jin Taekyung’s exposed skin and parts of his Fire Dragon Armor.

But he didn’t care.

No—there was no reason to.

Compared to everything that had happened so far, and everything still to come, this much pain was nothing.

*Grit.*

Through the faint pain, Jin Taekyung clenched his teeth.

At the same time, he planted a foot on the Dragon’s foreleg beneath him as if it were a stepping-stone, then thrust out a tightly clenched fist with all his strength.

*Flame-Extinguishing Divine Fist.*

*BAM!*

Compressed air exploded from the fist he drove forward like lightning.

The fierce heat packed into his knuckles swallowed the spraying blood, opening a new path beyond it.

*Whoooosh!*

It was a charge.

A charge in which one man staked everything—and a storm of hellfire that would melt and devour anything in its way.

*CRRRUNCH!*

A trail of flame carved through the air like an icebreaker smashing through a glacier.

The spearhead, driven deep into the enemy’s flesh and bone, erupted with lava as it climbed higher and higher.

The flames that rose in the wake of Jin Taekyung’s arrowing form burned so brilliantly and clearly that they seized the attention of everyone still locked in battle.

Human and monster alike.

No one was an exception.

Without realizing it, they lowered the blades in their hands or drew in their sharp claws and fangs.

Every living thing that had survived this horrific battlefield sensed it instinctively.

That rising flame, devouring the space around it, would decide all their fates.

If there were any exceptions, they were the only two beings who had faced each other from the beginning.

Leaving behind the vast battlefield and the countless eyes watching them, the Ancient Dragon and the human raced toward their final moment, gazing at each other like a scene from a myth.

*Jin Taekyung.*

*Morgoth.*

An inaudible whisper passed between them—not through their mouths, but through their eyes, across the open air.

Even though they couldn’t hear it, they could listen.

And even without speaking, they could feel.

And he could feel the emotions in the enemy’s eyes as they drew closer like the wind, as though defying the slowing of time.

And in this moment, Jin Taekyung saw a Dragon’s eyes filled with pain and fear.

*Yeah. This must hurt.*

With a thought that would never reach Morgoth, Jin Taekyung poured more strength into his charge.

He ran up the long, massive foreleg like a flight of stairs, heading for the head that loomed above him like a skyscraper.

*Like the people you killed with your own hands, or those who lost someone precious because of you.*

Jin Taekyung suddenly thought that he wished Morgoth’s pained roar—his every emotion and every ounce of suffering—could reach all those people.

Tens of millions had died.

Hundreds of millions had lost their families, friends, and homes.

That was why Jin Taekyung couldn’t stop.

It was the fuel for his will to keep moving forward.

*CRRRUNCH!*

Perhaps that was why.

His will had risen beyond the limits of his body.

The flame on his spearhead, which had been weakening along with the rapidly dwindling emptiness in his lower dantian, roared back to life. Part of his skin and muscle melted in the Dragon’s acidic blood, yet he couldn’t even feel the pain.

*Whooooom!*

The sky suddenly darkened, and gusts of wind slammed in from both sides.

Jin Taekyung didn’t waver in the slightest.

He simply swung the spearhead that had been cutting through the enemy’s body upward, straight at the two wings bearing down on him with enough force to crush a mountain.

*Shhhh.*

The rolling flames rose at an angle.

A single line, chillingly swift and savage.

In the arc of blue-black fire that suddenly appeared in the air were the Dragon’s two wings, which had ruled the vast sky and blanketed the earth for thousands of years.

*Shhk!*

—Kraaaaaa!

Pinning down the body thrashing with a muffled scream, Jin Taekyung dug his toes in.

*Fwoosh—BAM!*

Flamefire Path.

His form shot upward, propelled by a fierce explosion worthy of its name, and reflected in Morgoth’s pitch-black eyes.

No—that was wrong.

He soared into the sky like a fire dragon that had finally reached the time of its ascension. His form wasn’t merely reflected in those eyes; it overflowed from them.

—…!

Was this what it felt like when time stopped?

In the strange sensation, with every sound and movement around him gone, Morgoth watched Jin Taekyung.

He sensed the gaze sunk into an unfathomable depth, the blue-black light in his eyes unlike anything he had ever seen, and the countless fragments of emotion seeping through it.

And then came the realization, a step too late.

*Too late.*

Whether reason or instinct had reached that conclusion, Morgoth couldn’t say. But one thing was certain.

In this world where everything had stopped, that spearhead falling slowly, all alone, could neither be stopped nor avoided with any ability he possessed.

That left him only one path.

—Kraaaaaa!

His enormous jaws gaped open.

With the Ancient Dragon’s last struggle, heedless of death, the immense magical power and countless teeth lurking within its maw flashed toward a single human.

And at that very moment—

*Rrrrk.*

Jin Taekyung gripped the spear shaft with all the strength he had left.

The muscles throughout his body swelled. Fire raced through hundreds of acupoints and spread to every limb.

*Thump. Thump. Thump.*

His heart hammered furiously.

His lower dantian was empty enough to make the single recovery from leveling up seem meaningless, and his mind, already far beyond its limits, had been crying out from exhaustion for some time.

But he didn’t stop.

More precisely, there was no reason to stop.

*I can see it.*

In this new world painted in lines of every color, one trajectory shone brighter than all the rest.

Following the path he read through the Mind’s Eye, Jin Taekyung poured all his strength and will into the spearhead.

*Fwoosh—*

As time returned, the flame on the spearhead wavered.

But it wasn’t a sign of danger. It was a change—and an evolution—that took place in an instant.

*Shhhh.*

The wavering flame gathered into one.

It came together and connected, no longer a flame but a single line, as though it had become the spearhead itself. Then, at last, it settled.

It had advanced one step beyond the innate savagery of fire, becoming hellfire refined to the utmost degree.

And it was a peak Jin Taekyung had built on his own insight—a third path no one had ever taught him.

Fire Dragon Divine Spear.

Third Form.

*Fwoooosh.*

Space twisted.

The spearhead that had risen as if to cleave the sky—and the fire refined within it—gave off a terrifying heat.

Like another sun prepared to bring forth a new sky.

*Open Heaven.*

Amid the fierce shiver that seized his body and mind, Jin Taekyung brought down the hellfire spearhead, roaring silently.

*KABOOOOOM!*

The blue-black sun opened a world drowned in darkness.

* * *

They heard it, but didn’t hear it.

They saw it, but didn’t see it.

Among mountains of corpses and rivers of blood, countless living creatures watched an unbelievable sight unfold in the distance. In that moment, they all shared the same emotion.

A shudder.

They shuddered.

A blinding flash filled their vision, too bright to look at directly. A muffled roar blocked their ears. And yet everyone who survived could feel it clearly.

This long and terrible battle had finally come to an end.

The scene emerging beyond the slowly fading light proved their guess was right.

*Fwoooosh.*

A fierce wind swept through.

It wrapped around the enormous body tumbling down, silver blood spraying from it like a waterfall.

Yes. It was a fall.

And at the same time, the downfall of an Ancient Dragon that had lived for thousands of years.

What falls has wings. But his wings would never take flight again.

*KABOOOOOM!*

The earth shook. Dust billowed up and swirled across the area like a sandstorm in the desert.

And yet tens of thousands of eyes that had witnessed it all still faced the sky.

More precisely, they watched the lone being moving within the terrible stillness weighing down on the world.

*Step.*

He walked slowly through the air, as if stepping on an invisible staircase.

Even from a distance, he looked utterly exhausted. But no one there dared entertain the thought, or feel anything of the sort.

With the sky—its clouds torn away without a trace—at his back, he descended toward the ground against the falling sun. His very presence inspired an overwhelming awe.

As if he were something beyond human.

Or like an old image of someone the world would remember forever.

“…Sky.”

At the moment a nameless someone’s breathless murmur slipped from their lips, the people watching Jin Taekyung with trembling eyes realized one important thing they had forgotten.

They had won.

No—they, all of humanity, had won.

And the one who had led them was a new savior of humanity.
```
