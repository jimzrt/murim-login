<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1163.txt",
      "sha256": "164102f2e65990e4d08babd7992f207a2f2bd7f339ff1e60274e90624874ebdf",
      "bytes": 12851
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ffcf5edc7b1ca0eee888461c80dfabc439ac54f09cb85caa14f9702f1330ed7",
      "bytes": 603
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a2ca50a70b37521e504ee679d35c1d593ed1084caf47344d7bb2878103f7e5f8",
      "bytes": 247649
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "817a7ff963a76619a67e516b363cb160bd7d3b2c22b15b74b15c3dce18bf5841",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8653cd0f652e3cdbb3a3b5b09ef476ca16a8e9d8d09e9eac2a9a54225efeb73d",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "88f33946c8125b845f1b6514837d3fa6b7a2e2401f8c9af28209574d01f70159",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "309ec5cc197376c14521eddcf1901b0d4cea5d1674ed4d85a46345a88dc9a20c",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c24c5f4baa10652e407bb9a5f73cdab31aee2834b80b8385240e0623c25cab1d",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "65698c3e69c6f2bdb2615952693b90891662d73b4b25a147d9017f4efcbe617e",
      "bytes": 768
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "59a4543334ba7c2cce9aac1771d709310b7879c6fbd0a17977ad5c446460aec0",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "06cce74fac148e983deb4f44cb5bb7dea040e7529b5cce61b28a2bcc337025a0",
      "bytes": 294318
    }
  ],
  "estimated_tokens": 9891
}
-->

# Durable State Update — Chapter 1163

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
1 and safe_through 1163. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1163. Profile updates may replace only one
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
  "chapter": 1163,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1163,
    "continuity_sources": [1163],
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
    "Morgoth holds the damaged but living Skeleton King as a trophy.",
    "Jin regards the Skeleton King as his friend and is fighting Morgoth to protect him.",
    "Jin's spear strike scorched Morgoth; Morgoth summoned thousands of Dragon-tooth soldiers.",
    "Pai Chen is among Morgoth's Dragon-tooth soldiers."
  ],
  "continuity_sources": [
    1162
  ],
  "open_questions": [
    "Why is Pai Chen among Morgoth's soldiers?",
    "What will happen in the confrontation between Jin and Morgoth?"
  ],
  "safe_through": 1162,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 장로     | **Elder**                                    |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 외눈박이 | **One-Eyed** | Epithet of Carus, who has only one eye. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 워리어 | **Warrior** | Skeleton subtype mentioned alongside Soldiers and Mages. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 슈마허 | **Schumacher** | Surname of Germany's S-rank Hunter Joel Schumacher. |
| 조엘 | **Joel** | Given name of Joel Schumacher. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |
| 용아병 | **Dragon-tooth soldiers** | Guardians born of Dragons and serving them. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 슈마허 | rescuer to endangered allied Hunter | you | casual and blunt | Jin asks Schumacher whether he intends to die after arriving between him and the Minotaur Lord. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1162
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1162
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1157
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1162
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1162
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1162
- **Aliases:** None
- **Role:** Morgoth is a Dragon and the sovereign of a vast palace who seeks to recruit the Skeleton King as his Guardian.
- **Personality:** Composed and intellectually curious, he pursues the unknown with consuming greed and will abandon restraint when confronted with something unprecedented.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth offers the Skeleton King the role of Guardian, which the Skeleton King refuses.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1138
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1163화



이별은 늘 슬픔과 아쉬움을 낳는다.

그것이 가까웠던 누군가의 죽음으로 인한, 영원한 이별이라면 더더욱.

하지만 결코, 이런 식의 재회를 원한 것은 아니었다.

“……파이 첸?”

신음처럼 흘러나온 한 사람의 이름.

그리고 먼 거리에서도 단번에 알아볼 수 있을 만큼 낯익은, 그러나 그 어느 때보다 낯설게 느껴지는 얼굴.

아니.

얼굴들.

“아주 오래전, 내가 머무르던 세상에도 유난히 특출 난 존재들이 있었지. 용사 혹은 영웅으로 불리던 자들 말이야.”

석상처럼 굳어 버린 진태경의 귓가로, 옛 추억에 흠뻑 젖은 악룡의 목소리가 흘러들었다.

“처음에는 성가시더군. 별것 아닌 이유로 레어까지 찾아와 무례한 행동을 저지르는 게 썩 마음에 들지 않았거든.”

모르고스는 그들의 행동을 좀처럼 이해하지 못했다.

고작 도시 몇 개를 불태우고, 왕국 하나를 없앴다고 자신의 레어까지 찾아와 행패를 부리다니.

“적어도 어느 날, 한 인간을 만나기 전까지는 그랬지.”

그는 앞서 찾아온 수백 명의 영웅 중에서도 특별했다.

강했고, 강인했으며, 누구보다 처절하게 싸웠다.

그래서였을까.

여느 침입자들이 그러했듯, 제대로 된 시신조차 남기지 못하고 한 줌의 핏물이 되어 버린 그의 죽음에 모르고스는 처음으로 아쉬움을 느꼈다.

마음 깊은 곳에서 고개를 든 강렬한 소유욕도 함께.

“그때부터였지. 본격적으로 ‘전리품’을 모으기 시작한 게.”

그저 차갑고 단단하기만 한 금은보화 따위가 아닌, 각각의 기억과 빛을 간직한 특별한 전리품들.

인간, 요정, 난쟁이. 때로는 몬스터.

굴복시킬 수 있다면 굴복시켰고, 어떤 회유에도 응하지 않는다면 죽여서라도 곁에 두었다.

가장 귀중한 전리품이자, 가디언(Guardian)이라는 이름으로.

그리고 이 흥미로운 수집은, 지구라 불리는 낯선 세계에서도 이어지고 있었다.

“아직 미완성이지만, 재료가 좋으니 결과물도 훌륭하더군.”

“……!”

“어떤가, 내 새로운 가디언들이?”

흡족함이 묻어 나오는 그 물음에 진태경은 대답하지 않았다.

아니, 할 수 없었다.

어느덧 용아병들의 선두에 나와 자리한, 핏기 하나 없이 창백한 얼굴들을 바라보며 마음속으로 뇌까리는 것밖에는.

‘파이 첸, 조엘 슈마허, 파블로 알바토레스…….’

일곱 개의 이름.

일곱 명의 S급 헌터.

한 나라를 대표하는 영웅이자 서로의 등을 맡길 만큼 믿음직한 전우였던 이들.

지난 며칠에 걸쳐 이어진 흑룡의 대침공 속, 시체조차 찾지 못하고 장렬히 산화했다는 그들이 지금 이 자리에 나타났다.

죽어서도 안식을 누리지 못한 채.

영혼마저 빼앗긴 꼭두각시와 같은 모습으로.

스르릉.

날 선 검을, 철퇴를, 할버드와 방패를 들어 올리고 활시위를 겨눈다.

다른 누구도 아닌 진태경에게.

아무것도 보이지 않던 어둠 속에서, 그들 모두의 앞을 밝혀 주던 유일한 등불이자 희망을 향해.

스아아아.

차갑게 식은 바람이 초토화된 대지를 스친다.

어느덧 사방을 빈틈없이 포위한 괴물들의 살의(殺意)가 칼날이 되어 휘몰아치고, 하나의 거대한 벽이 되어 주인의 앞을 가로막은 일천의 용아병들 너머에는 하얗게 웃고 있는 악룡이 있다.

“자, 시작해 볼까.”

그리고 그 한마디가, 모든 것의 시작을 알리는 신호탄이었다.

드드드드득!

하늘과 땅을 뒤흔들며 끝없이 쏟아지는 괴물들의 파도.

그와 동시에, 차갑게 굳어 있던 진태경이 두 눈을 반개(半開)했다.

화륵, 콰아아아!

창날을 휘감으며 터져 나온 검푸른 화염이, 온 사방을 아득한 빛으로 물들였다.



* * *



서걱!

벤다.

퍼걱! 푸푸푹!

찌른다.

콰직!

부수고, 짓이긴다.

그리고.

콰드드드득!

나아간다.

띠링. 띠링. 띠링.



-[Lv98. 강화된 미노타우로스 워리어]를 처치하셨습니다!

-[Lv110. 강화된 트윈 헤드 오우거]를 처치하셨습니다!

-[Lv120. 강화된 데스 나이트]를 처치하셨습니다!

……

-힘의 격차에 따라 획득 경험치가 감소합니다!

-소량의 경험치를 획득했습니다!



진태경은 참았던 호흡을 내뱉었다.

쉴 새 없이 귓가를 울리는 종소리는 점점 멀게 느껴지고, 괴물들에게서 흘러나오는 악취와 괴성은 그 어느 때보다 가까우면서도 선명하다.

-구워어어어!

불현듯 수백 개의 머리 위로 드리워진 그림자.

걸어 다니는 마천루나 다름없는 외눈박이 거인, 사이클롭스(Cyclops)가 천지를 울리는 포효와 함께 두 주먹을 내리찍는다.

퍼어엉!

압축된 공기가 폭발하고, 주먹 끝에 실린 태산과도 같은 힘이 맞닿은 모든 것을 짓누르며 터트렸다.

단 하나, 반드시 쓰러트려야 할 누군가를 제외한 모두를.

-……!

마침내 거인이 제 손바닥보다도 작은 그 인간을 발견했을 때는, 검푸른 화염이 실린 창극(槍戟)이 하나뿐인 눈동자를 파고드는 중이었다.

퍼걱!

마치 두부를 가르듯 부드럽게 눈동자를 관통한 창날이, 동시에 그 끝에 담겨 흘러 들어간 끔찍한 열기가 거인의 뇌를 녹이고 거대한 몸뚱어리를 쓰러트린다.

후우우웅, 콰앙!

자욱하게 피어오르는 흙먼지.

절명한 거인의 몸에 깔린 괴물들의 비명이 울려 퍼지고, 일순간 가려진 시야에 표적을 놓친 몬스터들이 머뭇거렸다.

그것이 자신들의 생애 마지막 실수인지도 인지하지 못한 채.

슈확!

먼지구름이 반으로 갈라졌다.

아니, 증발했다.

그와 동시에 공간을 가르며 빛살처럼 날아든 한 자루의 창이, 앞선 거대한 폭발 속에서도 살아남은 몬스터 군단을 지휘하던 리치(Lich)들을 휩쓸었다.

콰드드드득!

수십 번에 걸쳐 중첩 시킨 방어 마법도, 눈 깜짝할 사이에 발현되는 블링크 마법도 소용없었다.

정확히는 창날에 실린 미증유의 거력이 그 모든 것을 무의미하게 만들었다.

압도적이라는 표현조차 부족한, 실로 경이롭기 그지없는 힘과 속도.

“재미있는 세상이야. 정말로.”

고대 신화 속 주인공처럼 전장을 지배하는 진태경을 바라보며, 모르고스는 진심으로 감탄했다.

지난 수천 년간, 무수한 강자를 직접 보고 겪은 그다.

하지만 천 년에 가까운 수명을 누리는 요정 장로도, 바위산의 축복을 받았다는 난쟁이 왕과 대륙 제일이라 불리던 인간 기사도 저런 무위를 보여 주진 못했다.

아니, 그들은 턱없이 부족했다.

“아스모데우스여, 이제야 조금은 이해할 수 있을 것 같군. 그대가 실패했던 이유를.”

이 낯선 세상의 인간들은 강하다.

모르고스의 능력으로도 도무지 파악할 수 없는 신비한 힘으로 강해지고, 그중에서도 선택받은 극소수의 인간들은 주어진 한계를 아득히 벗어난 초인으로 거듭난다.

지금은 죽은 것이나 다름없다는 천태민처럼.

혹은 무모하리만치 용맹한, 저 인간족의 젊은 영웅처럼.

그렇기에.

우우웅.

반드시 짓밟아야만 한다.

드높은 긍지를 내려놓는 한이 있더라도.

“아이스 월(Ice Wall).”

짧은, 그러나 그 어떤 종족도 따라올 수 없는 강력한 마법의 힘이 실린 스펠(Spell)이 전장에 울려 퍼진 그 순간.

스아아아.

모든 것을 얼려 버리는 극한의 냉기가 수백 미터의 거리를 가로질러 발현되었다.

그리고 그 끝에, 끝없이 밀려드는 상위 몬스터들을 한낱 양 떼로 전락시켜 버린 한 인간이 있었다.

콰드드득!

불현듯 대지 위로 드리워진 거대한 그림자.

무려 수 미터의 두께와 그 열 배에 달하는 높이로 사방을 감싸며 솟구친 빙벽은 하나의 감옥에 가까웠다.

오직 진태경을 가두기 위해 마련된 감옥이자, 그의 죽음을 위해 마련된 관.

“헬 파이어(Hell Fire).”

화아아악.

하늘이 붉게 물들었다.

동시에 먹구름 사이로 고개를 내민 화염의 구가.

그 어떤 세상의 대마도사도 상상해 본 적 없을 만큼 거대하면서도 끔찍한 열기가 얼음의 벽 위로 내리꽂혔다.

콰아아아앙!

마주하는 것만으로도 눈이 멀어 버릴 것 같은 맹렬한 섬광.

말 그대로 지옥의 업화(業火)라 불릴 만한 화염은 빙벽을 녹이고 그 안에 갇혀 있던 모든 것을 불태웠다.

미끼로 던져진 일천 마리의 몬스터와, 그로 인해 미처 마법의 범위를 벗어나지 못한 어느 인간도 함께.

분명, 그랬어야 했다.

투둑. 투두두둑.

숯 더미가 된 몬스터들의 사체 속에서 시작된, 아주 작은 흔들림.

이내 그 틈새로 모습을 드러낸 낯익은 얼굴을 확인한 모르고스는 조용히 입술을 핥았다.

‘견뎠다고? 조금 전의 그 마법을?’

일반적인 헬 파이어가 아니었다.

그만의 지식으로 기존의 위력과 한계를 극대화시킨, 심지어 전력을 다한 공격이었다.

직격당한다면 동족인 드래곤조차 치명상을 피할 수 없을 정도의 마법.

그런데 몸을 피할 수도 없는 상황에서 그 열기를 고스란히 버텨 내다니.

모르고스는 낮게 깔린 목소리로 뇌까렸다.

“이건…… 조금 곤란한데.”

아니, 어쩌면 그 이상일지도 모른다.

예상을 뛰어넘는 상황 뒤에는 언제나 알 수 없는 위험이 도사리고 있으니까.

그리고 그 위험은, 모르고스가 생각했던 것보다도 크고 빨랐다.

드득, 쾅!

굉음과 함께 발끝에서 터져 나온 폭발.

염화일로(炎火一路)라는 명칭에 담긴 뜻처럼, 진태경은 검푸른 화염의 길을 만들어 내며 쇄도했다.

서걱, 콰드드득!

앞을 가로막은 모든 것들이 갈라지고 부서진다.

사방에서 끝없이 밀려드는 몬스터 군단이 파도와 같았다면, 그는 파도를 관통하며 쏘아지는 하나의 창날이었다.

일격. 

또 일격.

내뻗는 주먹에 오우거의 머리가 터져 나가고, 채찍처럼 휘어진 발끝에 격중당한 데스 나이트는 두 번 다시 일어나지 못했다.

그리고 어느 순간, 진태경은 녹색 피를 흩뿌리며 쓰러지는 몬스터들의 눈동자에서 익숙한 무언가를 보았다.

공포.

그건 공포였다.

띠링. 띠링. 띠링.



-[일기당천]의 발동 효과를 충족하셨습니다!

-칭호, [일기당천]의 효과로 인해 적들이 크게 위축됩니다!

-칭호, [일기당천]의 효과로 인해 [위압]이 크게 증가합니다!

-당신의 [위압]에 두려움을 느낀 적들이 뒷걸음치기 시작합니다!



단단한 둑이 허물어진다.

오직 살육만을 갈망하던 본능이 옅어지고, 그 빈자리를 채운 것은 두려움이라는 낯선 감정이다.

-그워어어어!

어느덧 흉포함이 사라진 괴성과 함께 등을 돌려 멀어지는 몬스터들을, 진태경은 구태여 쫓지 않았다.

그에게는 아직 남은 적들이 있었으니까.

그리고 곧 시작될 전투야말로, 오늘 이 자리의 승패는 물론 앞으로의 모든 것을 결정지을 테니까.

철벅. 철벅.

사방에 고인 피 웅덩이를 밟으며 나아가는 힘없는 발걸음.

아직도 철탑처럼 자리를 지키고 있는 일천의 용아병들 너머, 그런 진태경의 모습을 물끄러미 바라보던 모르고스가 불쑥 입을 열었다.

“지쳤군.”

진태경이 피곤한 음성으로 대답했다.

“덕분이지.”

“그 상태로 나를 쓰러트릴 수 있을 거라 생각하나?”

“글쎄, 혹시 모르지. 네 앞에 있는 놈들만 치워 준다면.”

“어쩌면, 그래. 내가 조금 더 어리석었다면 그랬을지도 모르겠군.”

깊게 가라앉은 눈빛으로 진태경을 응시하며, 모르고스가 말을 이었다.

“하지만 안타깝게도 이미 결심했다네. 오늘 이 자리에서만큼은 잠시 긍지를 내려놓기로.”

철컥.

모르고스의 손짓에 따라 용아병들이 걸음을 내디딘 그 순간.

화아아악!

저 멀리, 몬스터 군단이 사라진 지평선 너머로 섬광이 번뜩였다.
```

## Final English reading copy

```markdown
# Chapter 1163

Partings always brought sadness and regret.

All the more so when it was a permanent farewell caused by the death of someone close.

But I had never wanted to reunite like this.

“……Pai Chen?”

A name slipped out like a groan.

And a face so familiar I could recognize it at a glance from far away, yet more unfamiliar than ever.

No.

Faces.

“Long ago, there were some especially exceptional beings in the world where I lived. The ones called warriors or heroes.”

The wicked Dragon’s voice, steeped in old memories, reached Jin Taekyung’s ears as he stood frozen like a statue.

“At first, they were a nuisance. I didn’t much care for them coming all the way to my lair to cause trouble over some trivial matter.”

Morgoth could never quite understand their behavior.

All he had done was burn a few cities and wipe out a kingdom, and they came all the way to his lair to make a scene.

“At least, not until I met one human.”

He was exceptional, even among the hundreds of heroes who had come before him.

Strong, tough, and more desperate in battle than anyone.

Perhaps that was why.

When he died, leaving behind nothing but a pool of blood—not even a proper corpse, just like all the other intruders—Morgoth felt regret for the first time.

And, deep in his heart, a powerful desire to possess him rose with it.

“That was when I began to collect ‘trophies’ in earnest.”

Not mere cold, hard gold and jewels, but special trophies that retained their own memories and light.

Humans, elves, dwarves. Sometimes monsters.

If they could be made to submit, he made them submit. If they refused every offer, he killed them just to keep them by his side.

His most precious trophies, under the name of Guardians.

And this fascinating collection had continued in an unfamiliar world called Earth.

“They’re still unfinished, but the material is good, so the results are excellent.”

“……!”

“What do you think of my new Guardians?”

Jin Taekyung didn’t answer the question, which was brimming with satisfaction.

No—he couldn’t. All he could do was stare at the faces, pale and bloodless, now standing at the head of the Dragon-tooth soldiers, and mutter their names to himself.

*Pai Chen, Joel Schumacher, Pablo Albatroses……*

Seven names.

Seven S-rank Hunters.

Heroes who represented their countries, comrades reliable enough to entrust with one another’s backs.

During the Black Dragon’s great invasion over the past several days, they had been reported to have perished gloriously, their bodies never even found.

And now they stood here.

Unable to rest even in death.

Reduced to puppets whose very souls had been stolen.

*Shing.*

They raised keen-edged swords, maces, halberds, and shields. They drew their bows.

Not at anyone else, but at Jin Taekyung.

The one who had been their only beacon in the darkness, lighting the way before them all—their hope.

*Fwoooosh.*

A cold wind swept across the devastated land.

The murderous intent of the monsters, now surrounding them on every side without a gap, surged like blades. Beyond the thousand Dragon-tooth soldiers, forming one enormous wall before their master, the wicked Dragon smiled white as snow.

“Now, shall we begin?”

And that one line was the signal that announced the start of everything.

*Rumble-rumble-rumble!*

A wave of monsters poured down without end, shaking heaven and earth.

At the same time, Jin Taekyung, who had stood frozen in the cold, half-opened his eyes.

*Whoosh—KABOOM!*

Blue-black flames burst out, coiling around his spearhead and flooding the whole area with blinding light.

* * *

*Slice!*

He slashed.

*Thwack! Thud-thud-thud!*

He stabbed.

*Crunch!*

He smashed and crushed.

And then—

*Rumble!*

He pushed forward.

*Ding. Ding. Ding.*

> **System**
>
> You defeated the Lv. 98 Enhanced Minotaur Warrior!
>
> You defeated the Lv. 110 Enhanced Twin-Headed Ogre!
>
> You defeated the Lv. 120 Enhanced Death Knight!
>
> …
>
> EXP gained is reduced due to the difference in strength!
>
> You gained a small amount of EXP!

Jin Taekyung let out the breath he’d been holding.

The chimes ringing incessantly in his ears seemed to grow more distant. The stench and roars pouring from the monsters had never been closer or clearer.

“Gwoooar!”

Suddenly, a shadow fell across hundreds of heads.

The Cyclops, a one-eyed giant as tall as a walking skyscraper, slammed both fists down with a roar that shook heaven and earth.

*BOOM!*

Compressed air exploded. The mountain of force behind its fists crushed and burst everything it touched.

Everything except the one person it absolutely had to bring down.

By the time the giant finally spotted that human, smaller than its palm, a spearhead wreathed in blue-black flames was already boring into its single eye.

*Thud!*

The spear pierced its eye as smoothly as if slicing through tofu. At the same time, the dreadful heat flowing through the spearhead melted the giant’s brain and sent its massive body crashing down.

*Whoooosh—BOOM!*

A thick cloud of dust billowed upward.

Monsters caught beneath the dying giant screamed. Those who lost sight of their target in the momentary dust hesitated.

Not realizing that this was the last mistake they would ever make.

*Fwoosh!*

The cloud of dust split in two.

No—it evaporated.

At the same time, a spear shot through the air like a ray of light, sweeping through the Liches commanding the monster army that had survived the massive explosion.

*Rumble!*

Dozens of layers of defensive spells were useless. So were Blink spells cast in the blink of an eye.

More precisely, the unprecedented force carried by the spearhead made them all meaningless.

A power and speed so astonishing that even “overwhelming” fell short.

“What an interesting world. Truly.”

Watching Jin Taekyung dominate the battlefield like the hero of an ancient myth, Morgoth was genuinely impressed.

He had personally seen and fought countless powerful beings over the past several thousand years.

But neither an elven Elder who had lived nearly a thousand years, nor a Dwarf king blessed by the rocky mountains, nor the human knight called the greatest on the continent had ever displayed such martial prowess.

No. They had been nowhere close.

“Asmodeus, I think I’m beginning to understand why you failed.”

The humans in this unfamiliar world were strong.

They grew stronger through some mysterious power Morgoth couldn’t begin to understand. And a tiny handful of those humans, chosen from among the rest, became superhumans who far surpassed their given limits.

Like Cheon Taemin, who was as good as dead now.

Or the young hero of the human race, recklessly brave as he was.

And so—

*Vwoom.*

He had to crush them.

Even if he had to set aside his pride.

“Ice Wall.”

A short Spell, yet one imbued with powerful Magic no other race could match, rang across the battlefield.

*Fwoooosh.*

An extreme cold that froze everything spread across hundreds of meters.

At its far end stood a human who had reduced the endless flood of high-level monsters to a mere flock of sheep.

*Rumble!*

Suddenly, an enormous shadow fell across the ground.

An ice wall erupted around him, several meters thick and ten times as tall, enclosing him on every side. It was closer to a prison.

A prison built solely to hold Jin Taekyung—and a coffin prepared for his death.

“Hell Fire.”

*Fwoooosh.*

The sky turned red.

At the same time, a sphere of flame emerged from between the dark clouds.

An unbearable heat, so vast no Grand Mage in any world had ever imagined it, crashed down upon the ice wall.

*KABOOM!*

A blinding flash, fierce enough to make your eyes go blind just by facing it.

The flames, worthy of being called the fires of Hell itself, melted the ice wall and burned everything trapped inside.

The thousand monsters thrown away as bait—and one human who hadn’t managed to escape the spell’s range in time.

That was what should have happened.

*Tap. Tap-tap.*

A tiny tremor began among the monsters’ corpses, now reduced to piles of charcoal.

When a familiar face emerged from the gaps, Morgoth quietly licked his lips.

*He endured it? That spell just now?*

That hadn’t been ordinary Hell Fire.

He had used his knowledge to maximize its power and limits, and he had even put his full strength behind the attack.

A direct hit would have left even another Dragon with a potentially fatal wound.

And Jin Taekyung had withstood all that heat, without even being able to dodge.

Morgoth muttered in a low voice.

“This is…… a little troublesome.”

No, perhaps more than that.

An unpredictable danger always lurked behind a situation that exceeded expectations.

And this danger was bigger and faster than Morgoth had thought.

*Crack—BOOM!*

An explosion burst from Jin Taekyung’s toes with a thunderous roar.

Just like the meaning contained in the name Flamefire Path, he surged forward, blazing a trail of blue-black flames.

*Slice, rumble!*

Everything blocking his way was split apart and broken.

If the monster army flooding in from every direction was a wave, he was a single spearhead piercing through it.

One strike.

Then another.

An ogre’s head burst beneath a punch. A Death Knight struck by his whip-like kick never got back up.

And at some point, Jin Taekyung saw something familiar in the eyes of the monsters collapsing as they sprayed green blood.

Fear.

It was fear.

*Ding. Ding. Ding.*

> **System**
>
> You have met the activation requirements for One Against a Thousand!
>
> The enemies are greatly intimidated by the effect of the Title One Against a Thousand!
>
> Intimidation has greatly increased due to the effect of the Title One Against a Thousand!
>
> Enemies who fear your Intimidation are beginning to retreat!

A sturdy dam crumbled.

The instinct that had craved nothing but slaughter began to fade, and a strange emotion called fear filled the space it left behind.

“Gwoooar!”

The monsters turned their backs and fled, their roars no longer so ferocious. Jin Taekyung didn’t bother to chase them.

He still had enemies left.

And the battle about to begin would decide not only the outcome here today, but everything that came after.

*Squish. Squish.*

His weary steps splashed through pools of blood on the ground.

Beyond the thousand Dragon-tooth soldiers still standing like iron towers, Morgoth had been watching Jin Taekyung in silence. Suddenly, he spoke.

“You’re tired.”

Jin Taekyung answered in a weary voice.

“Thanks to you.”

“Do you think you can defeat me in that state?”

“Who knows? Maybe. If you’d just clear away the guys in front of you.”

“Perhaps. If I were a little more foolish, I might have.”

Morgoth fixed his gaze on Jin Taekyung, his eyes sunk deep, and continued.

“But I’m afraid I’ve already made up my mind. Today, just this once, I’ll set aside my pride.”

*Clank.*

The Dragon-tooth soldiers stepped forward at Morgoth’s gesture.

*Fwoooosh!*

Far away, beyond the horizon where the monster army had vanished, a flash of light flared.
```
