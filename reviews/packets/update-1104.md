<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1104.txt",
      "sha256": "b11e34c2b56195f2c5544ac593837693747834ac4ae67141822c4196d4188a2b",
      "bytes": 11757
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6678b1f3039d5050d2544a894feeb6ee73020a06545857cb2a6b2f1ac5e80d8f",
      "bytes": 1444
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "fa95b5dfd25c52ef301e023db0b8939b429214682fd66705ad7ec0a985452d76",
      "bytes": 907
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "32cceb293846da3436b48901bf402cdf1c0ea1b093d52bbf3fcaf4fe6b977ab7",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6bf5765f6e0801db5a5af25df34fc8ae10db454fc7ff344d3d527977261aecd7",
      "bytes": 623
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "a3b12cb45dc6d5720d72b3969b5bd3d6795c2a62aa39f9e38a920c0b724d8234",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f15b6bb616e0bd10e582c2c20db1381f3647dfe2374b0b254aed2c21ef827565",
      "bytes": 287948
    }
  ],
  "estimated_tokens": 9124
}
-->

# Durable State Update — Chapter 1104

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
1 and safe_through 1104. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1104. Profile updates may replace only one
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
  "chapter": 1104,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1104,
    "continuity_sources": [1104],
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
    "Dark Heaven and the Potala Palace are attacking Xining; the siege is underway.",
    "The Blood Lord has coordinated pressure across the gates to exhaust the defenders and create an opening.",
    "The Dalai Lama leads roughly ten thousand Potala Palace monks toward the North Gate to attack Jeok Cheongang and avenge the Palace’s ancestral grievance.",
    "The Blood Lord expects allies to arrive by river from the east; a skeletal eagle signaled their approach.",
    "Xining’s wall has been breached; fighting continues at the breach.",
    "Cheongpung intercepted an attack aimed at Taekyung and is missing after the blast.",
    "The Blood Lord is approaching Taekyung."
  ],
  "continuity_sources": [
    1102,
    1103
  ],
  "open_questions": [
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What happened to Cheongpung after he intercepted the attack?"
  ],
  "safe_through": 1103,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1103
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but resents the Lord’s apparent special interest in Jin Taekyung, whom he resolves to kill even if it means defying the Lord’s command; he considers Taekyung and Cheongpung formidable adversaries.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1103
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1103
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1095
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1104화




철벅. 철벅.

피와 빗물. 그리고 무수한 시체로 뒤덮인 지면을 가로지르는 발걸음 소리가 유난히도 무겁게 울려 퍼진다.

수만.

아니, 적아를 통틀어 물경 십만을 넘어서는 이 거대한 전장의 한 가운데에서도 그의 존재감은 실로 압도적이었다. 

우우웅.

나아가는 발걸음을 따라 공간을 잠식해나가는 기운.

지금 이 순간에도 하늘에서 쉼 없이 쏟아져 내리는 빗줄기와 화살은 보이지 않는 기막(氣幕)에 가로막혀 튕겨 나갔고, 앞서 무너진 서쪽 성벽을 향해 돌격해 가던 암천의 교도들은 좌우로 갈라져 부복했다.

마치 무언가에 홀린 듯이, 여덟 글자의 교언을 읊조리며.

“천상천하.”

“만마앙복.”

그것은 경의였다.

이 세상의 진정한 지배자이자 자신들의 신에게 바치는, 더불어 그런 그가 친히 은총을 내린 단 여섯 명의 사도(使徒)에게만 허락된 경의.

그리고 몇 사람의 작은 뇌까림으로부터 시작된 교언은, 곧 거대한 울림이 되어 전장을 집어삼켰다.

……!

……!!

하나의 파문이 물살로 변하고, 이내 파도가 되어 사방으로 휘몰아친다.

거센 빗소리도, 먹구름 사이에서 번뜩이는 천둥도, 심지어는 허공을 뒤덮으며 쏟아져 내리는 화살조차도 그들의 입술 사이에서 흘러나오는 교언을 막을 수는 없었다.

“지금이다! 쳐라!”

“발시! 일제 발시하라!”

서걱! 푸푸푹!

칼날의 번뜩임과 함께 곳곳에서 솟구치는 목.

뿐인가.

몸뚱어리에서 떨어져 나온 팔과 다리가 흙탕물 속에 처박히고, 섬광처럼 날아든 화살들이 등과 허리에 박혔다.

하지만 그뿐이었다.

사지가 날아가도, 등을 관통한 화살촉이 가슴을 통해 삐져나와도 그들은 꿋꿋이 교언을 이어 갔다.

죽음의 그림자가 눈앞에 드리워지는 그 순간까지도.

“천상천하, 쿨럭. 만마앙복…….”

털썩.

핏물을 쏟아내면서도 기어코 교언을 읊고 나서야 죽음을 맞이하는 교도의 모습에, 앞서 그의 가슴에 검을 찔러 넣은 곤륜파의 도사가 입술을 파르르 떨었다.

“워, 원시천존이시여.”

도저히 무어라 형용할 수 없는 광신(狂信)의 물결.

한데, 이처럼 죽음조차 두려워하지 않는 광신도들이 곳곳에 가득하다.

아니, 이 광활한 전장을 새카맣게 물들인 적들 모두가 그러했다.

“이건…… 이건 도대체.”

누군가가 간신히 쥐어짜 낸 그 한 마디는 곧 모두의 심경이었고, 사람이 느낄 수 있는 극한의 두려움과 경악이 묻어 있었다.

철퍽. 투두둑.

불현듯 힘이 풀린 손아귀에서 미끄러진 병장기들이 진흙탕에 처박힌다. 

일순간 자신도 모르게 전의를 상실해 버린 몇몇 무림인들과 관군들은 흔들리는 동공으로 멍하니 적들을 바라보았다.

두려웠다. 몸서리가 쳐질 만큼 무서웠다.

거대하고도 흉포한 괴물들보다, 자신들과 같은 인간의 모습을 한 저들이.

인간이라면 누구나 지녔을 희로애락의 감정이 거세된 채, 맹목적으로 천주만을 따르는 저 미친 광신도들이.

그리고 그 중심이자 선두에, 핏빛 기운을 일렁이며 걸어오는 한 사람이 있었다.

“병신 같은 것들.”

나직한 조소(嘲笑)와 함께 드러나는 새하얀 이빨.

그와 동시에, 혈주가 부드럽게 내뻗은 손끝을 따라 지면을 뒹굴던 무수한 병장기들이 몸을 일으켜 세웠다.

아니, 새로운 주인의 명령과 함께 쏘아졌다.

어느새 얼어붙어 버린 적들을 향해.

“네놈들은, 살아 있을 가치도 없다.”

그 순간.

파파파팟!

수백여 개에 달하는 병장기들이 단숨에 공간을 갈랐다. 

무너진 성벽의 잔해를 휩쓸며 들이치는 강철의 파도.

그 아득한 섬광을 마주한 이들에게 더 이상의 선택지는 존재하지 않았다. 그들에게는 눈을 감을 시간도, 생애 마지막 숨결조차도 허락되지 않았다.

다만 그저, 커다랗게 뜨인 눈으로 들이닥치는 죽음을 바라볼 뿐이었다.

불현듯 자신들의 머리 위를 스쳐 지나가는, 한 줄기의 열풍(熱風)을 느끼며.

고오옹.

공간이 일그러진다. 

끔찍하리만치 거대한 열기가, 검푸른 색의 광염(光焰)이 모두의 시야를 물들었다.

그리고 마침내.

화륵, 콰아아아!

강철의 파도와 불의 벽이 만났다.

서로를 향해 맞닿고, 부딪혔다.

그 안에 간직한 미증유의 힘을, 아득한 섬광과 울림을 온 사방에 토해내며.

쿠구구구궁……!

무르익을 대로 무르익은 화산(火山)이 긴 잠에서 깨어나 포효한다면 이런 소리가 났을까.

아니면 태곳적 거인이 온 힘을 다해 숨을 토해내면 지금과 같은 폭풍이 휘몰아쳤을까.

그 누구도 알 수 없었다.

반경 수십여 장에 존재하는 모든 것을 뜨겁게 달구고 밀어내는 그 강렬한 빛과 충격파 속, 철탑처럼 우뚝 선 채 자리를 지키고 있는 두 사람을 제외하고는.

“그래, 오직 너만큼은 살아있을 가치가 있지.”

나직이 뇌까린 혈주가 수도(手刀)를 내리긋자, 서쪽 성벽을 휘감은 먼지구름이 단숨에 갈라지며 그 안에 감춰있던 것을 드러낸다.

전신이 피와 빗물로 흠뻑 젖어있는, 그럼에도 한 치의 흔들림 없이 그를 향해 새하얀 은백색의 창을 겨누고 있는 청년을.

“그렇기에, 더더욱 네놈을 살려둘 수 없게 되었지만.”

혈주가 찬탄 섞인 음성으로 청년을 응시했다.

“열화신룡(烈火神龍) 진태경.”

그리고 그 순간, 굳게 다물어져 있던 진태경의 입술이 열렸다.

“기습숭배는 고맙긴 한데…….”

푸푹.

어느새인가 몸 곳곳에 박혀 있는, 불의 벽을 관통하며 날아든 날붙이의 파편을 망설임 없이 뽑아낸 그가 말을 이었다.

“아무리 생각해 봐도 니 새끼는 살아 있을 가치가 없다. 그게 네가 뒈져야 하는 이유야.”

담담한 음성과는 달리 화염이 줄기줄기 쏟아지는 두 눈동자.

하지만 그런 진태경을 보며 혈주는 피식 실소를 흘렸다.

“가능하리라 생각하느냐? 그것도 지금과 같은 상태로?”

혈주의 말은 결코 과언이 아니었다.

당장 드러난 진태경의 몰골은 그 자체로 혈인(血人)이나 다름없었으니까.

물론 이는 지금껏 베어 넘긴 적들의 숫자를 생각한다면 당연한 일이었지만, 그렇다고 한들 그 역시 조금의 피해도 없는 것은 아니었다.

아니, 진태경 또한 분명 지치고 부상 입은 몸이었다.

지금 이 순간, 흡사 태산과도 같은 그의 등 뒤로 하나둘씩 몸을 일으키고 있는 다른 이들과 같이.

하지만 그는 조금도 두려워하지 않았다.

그보다 앞서 이미 충분히 두려워했기에. 

몸과 마음을 짓눌렀던 그 부정적인 모든 감정을 인정하고, 받아들였기에.

하여, 서서히 다가오는 혈주를 보면서도 희미하게나마 미소지을 수 있었다.

“물론 그렇게 생각할 수도 있겠지. 그런데 너, 그거 알고 있냐?”

“그게 무슨.”

“네 잘난 친구들도, 전부 나한테 그 지랄 떨다가 뒈졌다는 거.”

“……!”

“그거 다 사망 플래그야, 인마. 아, 이건 어차피 말해 줘도 못 알아듣나?”

뜻 모를 소리와 함께 소리 내어 웃는 진태경의 모습에, 혈주의 입가에 맺혀 있던 비웃음이 씻은 듯이 사라졌다.

“하지만 그 얼간이들과는 다르겠지. 네놈을 어설프게 살려 줄 마음 따위는 이미 진즉 지워 버렸으니까.”

스아아아.

보보(步步)마다 올올히 피어오르는 핏빛 기운.

붉게 번뜩이는 혈주의 두 눈동자에는, 오직 진태경만이 또렷이 비쳤다.

“넌, 오늘 죽는다. 틀림없이.”

“천주가 들으면 기분 나빠 하겠네. 그래도 말 잘 듣는 개새끼라고 나름 이뻐하면서 키웠을 텐데.”

“그분께서도 이해해 주실 거다. 오직 충심에서 비롯된 오늘의 이 선택을.”

“그래? 그냥 네 단순한 희망 사항이 아니고?”

“뭐?”

일순간 걸음을 멈춘 혈주의 귓가로, 진태경의 음성이 파고들었다.

“이해 못 할 것 같으니까, 걸리면 엿 될 것 같으니까 일단 저지르고 보려는 거잖아. 혹시 몰라서 대술사까지 멀리 치워 버리면서.”

“……!”

“왜 토끼 눈을 하고 바라보냐. 토 나오게 생겨 먹은 새끼가. 누가 보면 꼭 꿀잠 자다가 귀싸대기라도 맞은 줄 알겠네. 이미 꿈속에서 대충 그림이 그려지지 않았나?”

으득.

혈주는 자신도 모르게 이를 악물었다.

쉴 새 없이 쏟아지는 진태경의 도발적인 언사 때문이 아니라, 애써 외면하고 있던 진실이 송곳이 되어 폐부를 들쑤셨기 때문이었다.

“너도 충분히 알고 있잖아. 네 주인이, 그 빌어먹을 천주가 뭘 가장 원하고 있는지.”

반박해야 했다. 

자신이 신처럼 떠받드는 주인을 거침없이 모욕하고 그 저의를 의심하는 저 새파란 놈의 주둥이를. 지금 당장이라도 찢어 버리고 요사스러운 세 치 혀를 뽑아야 했다.

하지만 반박할 수 없었다.

열화신룡 진태경.

놈의 잔망스러운 입술 사이로 흘러나오는 모든 말들이 사실이라는 것을, 혈주 자신도 어렴풋이 느끼고 있었으니까.

언제부터인지는 모른다. 심지어는 그 이유조차 듣지 못했다.

그러나 오늘 이 자리까지 이어져 온 모든 상황은 단 한 가지의 뼈아픈 진실을 가리키고 있었다.

“네 주인이 무엇보다 원하는 건, 천하가 아니야. 너처럼 쓰다 버리는 사냥개들의 목숨 따위는 더더욱 아니고.”

귓속을 깊숙이 파고드는 것으로도 모자라, 뇌리를 뒤흔드는 저 목소리에 담긴 진실을.

“바로 나다. 오직, 나뿐이라고.”

“……!”

“그러니까, 어디 한번 죽여 봐. 이런 식으로라도 네 손을 빌려서 천주를 엿 먹일 수 있다면 난 뭐든 상관없으니까.”

바로 그 순간이었다.

서서히 붉게 달아오르던 혈주의 두 눈동자가, 새하얗던 동공이 완전한 핏빛에 뒤덮인 것은.

그리고 반경 십여 장에 걸쳐 널브러져 있던 무수한 시체들이 울컥 핏물을 토해 낸 것은.

솨아아아악.

빗물과 섞여 있던 그것이, 마치 살아있는 생물처럼 꿈틀거리며 한 사람의 발치로 모여들었다.

그와 동시에 어느덧 다시 나아가기 시작한 발걸음을 따라, 끊임없이 이어지고 뭉쳐지기를 반복하던 핏물이 종아리를 타고 전신을 감싸 안았다.

아니. 

그대로 흡수되었다.

아주 오랜 과거부터, 본래 한 몸이었던 것처럼.

스아아아.

몸속 깊은 곳에서 끝없이 솟아오르는 강인한 생명력과 힘을 느끼며, 혈주(血主)는 붉은 안광을 번뜩였다.

“유언, 잘 들었다.”

그 생각지도 못한 광경을 멍하니 바라보던 진태경이 입맛을 다시며 대꾸했다.

“그, 혹시. 조금 더 해도 될까?”

그 얼토당토 없는 물음에, 혈주는 대답했다.

거대한 핏빛 섬광으로.

쉬이이이익!

일순간 세상이, 붉게 물들었다.
```

## Final English reading copy

```markdown
# Chapter 1104

*Splash. Splash.*

The sound of footsteps crossing ground covered in blood, rainwater, and countless corpses rang out with unusual weight.

Tens of thousands.

No—even on this vast battlefield, where friend and foe together numbered well over a hundred thousand, his presence was utterly overwhelming.

*Vooooom.*

Qi spread through the space with every step he took.

Even now, rain and arrows poured unceasingly from the sky, only to bounce off an invisible barrier of energy. The Dark Heaven followers charging toward the collapsed western wall split to either side and prostrated themselves.

As if bewitched, they murmured a creed of eight words.

“Heaven above and earth below.”

“All demons bow!”

It was reverence.

Reverence offered to the true ruler of this world—their god—and permitted only to the six Apostles he had personally favored.

The creed, begun with a few quiet murmurs, soon became a tremendous roar that swallowed the battlefield.

……!

……!!

A ripple became a current, then a wave that swept in every direction.

The pounding rain, the thunder flashing between the dark clouds, even the arrows raining down to fill the sky—nothing could stop the creed pouring from their lips.

“Now! Attack!”

“Archers! Loose together!”

*Shhk! Thud-thud-thud!*

Blades flashed, and heads sprang up all over the battlefield.

And that wasn’t all.

Arms and legs severed from their bodies plunged into the mud. Arrows streaking in like flashes of light buried themselves in backs and waists.

But that was all.

Even when their limbs were cut off, even when arrowheads pierced their backs and poked out through their chests, they stubbornly continued reciting the creed.

Until the very moment death fell over them.

“Heaven above and earth below—cough. All demons bow……”

*Thud.*

The Dark Heaven follower collapsed. He’d kept reciting the creed to the bitter end, even as blood poured from him. The Kunlun Sect Daoist who had stabbed him through the chest trembled, lips quivering.

“P-Primordial Heavenly Venerable.”

A wave of fanaticism beyond words.

And there were fanatics like these everywhere, people who didn’t even fear death.

No—all the enemies, darkening this vast battlefield, were like that.

“This… What in the world is this?”

The one phrase someone managed to squeeze out was what everyone felt. It was steeped in the greatest fear and horror a person could feel.

*Splash. Clatter.*

Weapons slipped from suddenly slack hands and sank into the mud.

For an instant, some of the Murim warriors and imperial troops lost their will to fight without even realizing it. Their trembling eyes stared blankly at the enemy.

They were afraid. Terrified to the point of shuddering.

Not of some huge, savage monster, but of those who looked just like them.

Those mad fanatics, stripped of the joy, anger, sorrow, and pleasure every human being ought to feel, blindly following only the Lord of Heaven.

And at their center, at the head of their ranks, walked a man wreathed in rippling, blood-red qi.

“What a bunch of worthless bastards.”

His soft sneer revealed a row of white teeth.

At the same time, as the Blood Lord gently extended his fingertips, countless weapons that had been rolling across the ground rose upright.

No—they shot forward at their new master’s command.

Toward the enemies, frozen in place.

“You don’t deserve to live.”

At that moment—

*Pa-pa-pa-pat!*

Hundreds of weapons tore through the air in an instant.

A wave of steel surged through the ruins of the collapsed wall.

There was no choice left for those facing that blinding flash. They weren’t even granted time to close their eyes, let alone draw one last breath.

All they could do was stare, eyes wide, at the death bearing down on them.

And feel a streak of searing wind sweep over their heads.

*Gooooom.*

Space warped.

A heat so tremendous it was horrifying, dark blue light-flames, filled everyone’s sight.

And at last—

*Fwoosh—KRAAASH!*

The wave of steel met a wall of fire.

They collided head-on.

Unleashing all the unimaginable power they held within them—the blinding light and rumbling force—into every corner of the battlefield.

*Rumble-rumble-rumble……!*

Would this be the sound a fully awakened volcano made as it roared after a long sleep?

Or would a storm like this sweep over the land if an ancient giant exhaled with all its might?

No one could say.

No one, that is, except the two people standing tall as iron towers in the fierce light and shock wave that heated and drove back everything within dozens of yards.

“Good. You, at least, deserve to live.”

The Blood Lord murmured and brought down the edge of his hand. The cloud of dust coiling around the western wall split apart in an instant, revealing what it had concealed.

A young man, drenched from head to toe in blood and rain, stood perfectly steady, aiming a pure silver-white spear at him.

“That’s precisely why I can’t let you live.”

The Blood Lord watched the young man, admiration in his voice.

“Blazing Flame Divine Dragon, Jin Taekyung.”

At that moment, Jin Taekyung’s tightly closed lips parted.

“Thanks for the surprise worship, but……”

*Squelch.*

He pulled out the shards of blades that had somehow pierced his body in several places as they flew through the wall of fire, then continued:

“No matter how I look at it, you don’t deserve to live, you son of a bitch. That’s why you have to die.”

His voice was calm, but flames poured in streams from his eyes.

The Blood Lord gave a quiet laugh as he looked at him.

“Do you think you can do that? In your current condition?”

The Blood Lord wasn’t exaggerating.

Jin Taekyung’s appearance alone made him look like a man drenched in blood.

Given how many enemies he had cut down, that was only natural. But that didn’t mean he’d come away unscathed.

No. Jin Taekyung was undoubtedly exhausted and injured, too.

So were the others now rising one by one behind his back, which stood as imposing as a mountain.

But he wasn’t afraid at all.

He’d already been afraid enough before now.

He had acknowledged and accepted every negative feeling that had weighed down his body and mind.

And so, even as the Blood Lord approached, Jin Taekyung managed a faint smile.

“Sure, you could think that. But do you know what?”

“What are you talking about?”

“Your precious friends all pulled that same shit on me before they died.”

“……!”

“That’s what you call a death flag, you moron. Ah, would you even understand if I explained it?”

At Jin Taekyung’s laugh and incomprehensible words, the sneer at the Blood Lord’s lips vanished without a trace.

“But I’m different from those idiots. I gave up on the idea of halfheartedly letting you live long ago.”

*Fwoosh.*

Blood-red qi rose in wisps with every step.

In the Blood Lord’s red-glinting eyes, only Jin Taekyung was clearly reflected.

“You die today. No question.”

“Wouldn’t the Lord of Heaven be upset to hear that? He must’ve thought you were a good dog and taken a liking to you.”

“He will understand. This choice I make today comes from loyalty alone.”

“Is that so? Or is it just what you hope?”

“What?”

The Blood Lord stopped walking for an instant. Jin Taekyung’s voice slid into his ear.

“You think he won’t understand. You think you’ll be screwed if you get caught. So you’re doing it first and hoping for the best. Even going so far as to send the Grand Mage far away, just in case.”

“……!”

“Why are you staring at me like a rabbit caught in headlights? You look disgusting enough already. Anyone would think you’d just been slapped awake from the deepest sleep. Didn’t you already get a rough idea in your dream?”

*Crunch.*

The Blood Lord clenched his teeth without realizing it.

It wasn’t Jin Taekyung’s relentless taunts that made him do it. It was the truth he’d tried to ignore, stabbing into his heart like an awl.

“You know well enough, too. What your master—that damned Lord of Heaven—wants most.”

He had to refute him.

That insolent brat was openly insulting the master he worshiped like a god and questioning his intentions. The Blood Lord should tear his mouth apart right now and rip out that wicked tongue.

But he couldn’t refute him.

The Blazing Flame Divine Dragon, Jin Taekyung.

The Blood Lord had a vague sense that everything coming from that impertinent mouth was true.

He didn’t know when it had begun. He hadn’t even been told why.

But everything that had led to this moment pointed to one painful truth.

“What your master wants most isn’t the world. It sure as hell isn’t the lives of hunting dogs he uses and throws away, like you.”

It was more than a voice that burrowed into his ears. It was a truth that shook him to the core.

“It’s me. Only me.”

“……!”

“So go on, try to kill me. If I can screw the Lord of Heaven over by using you, I don’t care how it happens.”

That very instant, the Blood Lord’s eyes, which had been slowly reddening, turned completely bloodred, their white pupils swallowed up.

And countless corpses scattered across the ground within a dozen yards convulsed and spewed blood.

*Swoosh.*

The blood mixed with rainwater writhed as if it were alive and gathered at one man’s feet.

At the same time, as his footsteps began to move again, the blood kept flowing together, joining and merging, until it climbed his calves and wrapped around his whole body.

No.

It was absorbed into him.

As if it had always been part of him, from the distant past.

*Fwoosh.*

Feeling an unending well of vitality and strength rise from deep inside him, the Blood Lord’s eyes blazed red.

“I heard your last words.”

Jin Taekyung stared blankly at the unexpected sight, then smacked his lips and replied:

“Uh, maybe. Could I say a little more?”

The Blood Lord answered that ridiculous question with a massive flash of blood-red light.

*Whoooosh!*

In an instant, the world turned red.
```
