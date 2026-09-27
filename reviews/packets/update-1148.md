<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1148.txt",
      "sha256": "af0cde84526c587b979fb58fffb94918e3a978367b8bf02deaf3bf3ef7ef7537",
      "bytes": 11291
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "29f58a449b1bbe6f1a0306568d1212c2b682ed406b68a951fdf141ff0c033acb",
      "bytes": 1773
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c2c7c8b822a21edbf9fb8abda1956727086529d31a31ad49049d85289419fe9",
      "bytes": 246139
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "31cf9655ac4fda3ad43ed03cde229023cd6627ad4fe28fd6e9cc16becef25445",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "682ab084c003dacd2cc3b1f8172f0b5036008fd10c90602188387216f906e1d7",
      "bytes": 619
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b8239aad3d642a23dbd0b805b1ba3b79cd2f1e65b44042d7ea8377080af850ae",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6ccbd47eb77b857b178991f5a88b22cc439ad05212395ddc695bef279446b4c4",
      "bytes": 623
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "257407de7e9b43e3ce1b58f48fa34f229821a762af4674a63895c400ce920af6",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "84bf3127de2e16a15ed1c5331b7a597f9667aca0cc4451694f882723d846ca2d",
      "bytes": 291709
    }
  ],
  "estimated_tokens": 9109
}
-->

# Durable State Update — Chapter 1148

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
1 and safe_through 1148. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1148. Profile updates may replace only one
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
  "chapter": 1148,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1148,
    "continuity_sources": [1148],
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
    "Taekyung’s consciousness has returned to his body in Murim; he promised Jeok Cheongang he would return.",
    "Jeok Cheongang remains beside Taekyung and intends to protect him on the march to Tianshan.",
    "The coalition army of more than two hundred thousand is crossing the Taklamakan Desert toward Tianshan.",
    "The Grand Mage has been reborn through the Lord of Heaven’s grace and felt a wave; the Lord says the heavens have opened again as green light rises over jade.",
    "Taekyung has awakened at the bomb shelter battlefield, where Choi Minwoo and the Skeleton King are with more than two hundred Hunters.",
    "Thousands of monsters are attacking the Hunters; their weapons wield Auror, and Taekyung has joined the fight.",
    "Seven powerful, humanlike enemies appeared; Taekyung killed one, leaving six."
  ],
  "continuity_sources": [
    1146,
    1147
  ],
  "open_questions": [
    "What caused the wave that the Grand Mage felt and the Lord of Heaven acknowledged?",
    "What does the Lord of Heaven mean when he says the heavens have opened again?",
    "What danger awaits the coalition army at Tianshan?",
    "Who are the seven humanlike enemies, and what is the source of their unusually pure magical power?",
    "Why do the Hunters at the bomb shelter wield Auror?"
  ],
  "safe_through": 1147,
  "temporary_decisions": [
    "Render 仙界 as “realm of immortals.”",
    "Render 塔克拉玛干 as “Taklamakan Desert.”",
    "Render 스켈레톤 킹 as “Skeleton King” and 방공호 as “bomb shelter.”",
    "Render 오러 as “Auror” and 검기 as “Sword Energy.”",
    "Render 리자드맨 as “Lizardman,” distinct from 리자드 (“Charmeleon”)."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 조지아주 | **Georgia** | The U.S. state claimed as the Skeleton King's birthplace. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1146
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1094
- **Aliases:** None
- **Role:** A senior Dark Heaven sorcerer who directs its mages and participates in its plans to conquer the world.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** Cutting and sardonic, using taunts and pointed questions to challenge others.
- **Relationships:** Serves the Lord of Heaven and is an antagonistic peer of the Blood Lord, whose unilateral decisions anger her.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1147
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, and the Son of Heaven has formally enfeoffed him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1147
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 1147
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, whom he regards as a model of taking responsibility in a crisis; he is the maternal grandson of Cheon Taemin.

## Korean source

```text
＃1148화



무림인에게 있어 무위의 상승이란, 오감의 극대화뿐만이 아니라 집중력과도 직결된다.

주위에서 무슨 일이 벌어지건, 오직 일념(一念)으로 자신이 가진 것을 단숨에 쏟아부을 수 있는 무시무시한 집중력.

지금의 진태경이 바로 그랬다.

띠링.

귓가를 파고드는 익숙한 종소리.

그러나 이름난 장인이 벼려 낸 날붙이처럼 예리해진 그의 감각은 조금도 무뎌지지 않았다.

아니, 되레 더욱 날카로워졌다.

‘뭐지?’

갑작스럽게 등장한 정체불명의 네임드 몬스터들.

이미 그중 하나를 처치했지만, 기쁨보다 먼저 찾아온 건 창날을 통해 전해진 묵직한 감촉과 이유 모를 경계심이었고 이는 곧 더욱 쾌속해진 움직임으로 이어졌다.

팟.

잔상조차 남기지 않는 완벽한 이형환위(移形換位).

한 박자 늦게 쏘아진 여섯 줄기의 마력이 허무하게 허공을 관통함과 동시에, 진태경의 손에 들린 백염이 다시금 불길을 토해 냈다.

화륵, 콰아아아!

비스듬히 내리그어지는 창날을 따라 일그러지는 공간 속. 군청색의 화염이, 그 안에 실린 막대한 열양지기(熱陽之氣)가 또 하나의 네임드 몬스터를 베어 갈랐다.

정확히는, 그렇게 보였다.

다음 순간, 진태경이 창날을 통해 전해진 강렬한 반동을 느끼기 전까지는.

콰드드득!

“……!”

진태경은 크게 뜨인 눈으로 저 멀리 밀려나는 네임드 몬스터를 바라보았다.

또한 그와 동시에, 앞서 한 놈을 처단했을 때 느꼈던 이유 모를 경계심의 정체를 깨달았다.

‘단단하다.’

움직임이나 기세에 대해 논하는 것이 아니다. 원초적인 표현 그대로, 놈들의 신체가 더럽게 단단했다.

지금껏 숱한 적들을 쓰러트린 그조차도 쉽게 이해가 안 될 정도로.

‘백염으로도 완벽하게 베어 내지 못할 정도라니.’

백염이 어떤 물건인가.

초반에 이것저것 듬뿍 퍼 주던 시스템 보상이 아니었다면 구경도 못 했을 개사기템의 전형이요, 무림에서는 억만금을 줘도 구할 수 없는 무가지보(無價之寶)다.

심지어 최첨단 기술과 온갖 마법으로 떡칠한 현대의 아티팩트(artifact)조차도 무기 본연의 예리함과 강도는 백염을 따라가지 못한다.

그런데 저놈들의 몸뚱어리, 그중에서도 특히 상상 이상의 밀도는 지닌 뼈는 강기가 서린 백염의 창날로도 두부처럼 베어 낼 수 없었다.

물론 그 대가로 끔찍한 상처를 입었지만, 응당 쇄골부터 골반까지 일도양단 되었어야 할 적이 멀쩡히 서 있는 것부터가 진태경에게는 충격적이었다.

엄청난 회복 능력으로 순식간에 상처를 수복하고 있는 것은 덤이었고.

“어떻게 이게 가능하지?”

불현듯 입 밖으로 새어 나온 의문에, 어느덧 합류한 스켈레톤 킹이 대답했다.

“이 몸도 처음에는 그렇게 생각했는데, 생각해 보면 이해 못 할 수준도 아니더군.”

“왜?”

“네놈처럼 괴물 같은 인간도 있는데, 저런 놈들도 있을 수 있잖나.”

“장난하나. 나는 좀 예외지.”

“밥맛 없는 소리를 너무 당연하게 하는 거 아닌가?”

“밥맛을 논하다니, 아주 한국인 다 됐구만. 심지어 원래 컨셉은 외국인 아니었냐?”

합리적인 근거를 바탕으로 한 질문이었으나, 미국 조지아주 애틀란타 출신의 스톤 킹 씨는 스마트폰이라는 문명의 이기를 통해 많은 것을 배운 직후였다.

“한국계 미국인이야.”

“……못 본 사이에 말솜씨가 제법 늘었다, 너.”

“글쎄, 좋아진 게 말솜씨뿐만은 아닐걸.”

화아아악.

말이 끝나기가 무섭게 그를 중심으로 부풀어 오르는 거대한 마력.

과거와는 확연한 그 힘의 차이에 말없이 진태경이 눈만 깜빡이자, 스켈레톤 킹이 어깨를 으쓱해 보였다.

“왜, 이 몸의 강대함에 전율했나?”

“……도대체 그동안 무슨 일이 있었던 거야?”

“많은 일들이 있었지. 당장 이야기하는 건 무리겠지만.”

스켈레톤 킹의 말은 현실을 정확히 직시하고 있었다.

그리 멀지 않은 곳에서는 최민우가 헌터들을 지휘하며 몬스터들과 치열한 전투를 벌이고 있었고, 여섯 마리의 네임드 몬스터는 반원 형태로 그들을 포위하고 있었으니까.

스아아.

유형화된 마력이 안개처럼 일렁인다.

놈들의 안면 전체를 뒤덮은 해골 가면 뒤로, 단 한 줌의 감정도 깃들어 있지 않은 시선이 칼날처럼 두 사람을 찔렀다.

“목을 노려. 그나마 베어 내기 쉽다.”

어느새 등을 맞댄 스켈레톤 킹의 조언에, 진태경이 창대를 고쳐잡으며 대답했다.

“알아.”

“절반씩 맡자. 이 몸이 셋. 네가 셋.”

“가능하냐? 너 좆밥이잖아.”

“시건방진 인간 같으니. 혓바닥에 칼이라도 심어 놨나?”

그때였다.

투덜거리던 스켈레톤 킹이 문득 말을 멈추더니, 이내 들릴 듯 말 듯 한 음성으로 덧붙인 것은.

“그래도…… 반갑다.”

“뭐라고?”

“이렇게라도 다시 보게 되어서, 더럽게 반갑다고.”

뭐라 대꾸해야 할지 고민하던 진태경은 그냥 풀썩 웃어 버렸다.

그리고 어색한 침묵이 찾아오기도 전에, 지면을 박차고 적들을 향해 쇄도했다.

자신의 몬스터 친구가 그랬던 것처럼, 아주 작은 목소리로 대답하면서.

“그래, 나도.”

거의 동시였다.

쐐애애액!

전신을 휩쓴 바람이 목소리를 집어삼킨 것도.

소리마저 앞질러 쏘아진 진태경의 신형이, 스켈레톤 킹보다 한 걸음 앞서 놈들에게 도달한 것도.

쾅!

세 개의 검과 하나의 창날이 맞닿으며 터져 나오는 굉음.

하지만 백중세(伯仲勢)라 부를 수는 없었다. 놈들은 힘을 이기지 못해 물러났고, 진태경은 계속해서 나아가고 있으니.

쾅! 쾅! 콰드드득!

연달아 울려 퍼지는 굉음 속, 진태경의 힘과 속도를 따라잡지 못한 네임드 몬스터 하나가 무릎을 꿇었고 그는 더 이상 망설이지 않았다.

서걱!

창날을 통해 전해지는 묵직한 감각.

평소보다도 더욱 힘을 더한 일격에 새하얀 해골 가면을 쓴 목이 두둥실 떠오른다.

이미 양옆으로 두 개의 검이 휘둘려지고 있었으나, 반 박자 늦게 들이닥친 공격은 진태경의 몸에 닿지 못했다.

아니, 오히려 그보다 늦게 뻗어나간 그의 일권(一拳)이 먼저 허공을 후려쳤다.

퍼엉!

응축된 공기의 폭발.

마치 산을 때려 그 뒤의 소를 치듯이, 삽시간에 터져 나온 충격파가 놈들을 밀어내고 틈을 만들었다.

아주 찰나의, 그러나 생사의 갈림길이 될 수도 있는 빈틈을.

슈확!

그 일련의 움직임에는 별다른 예비 동작조차 필요 없었다.

진태경은 초인(超人)이라는 표현도 턱없이 부족할 정도의 신체 능력을 바탕으로 창을 던졌고.

퍼걱!

허공에서 내리찍듯이 쏘아진 창날은 또 다른 네임드 몬스터의 몸뚱어리를 꿰뚫었다.

주인이 의도했던 대로, 뼈와 뼈 사이를 정확히 파고들며.

콰드드득!

오우거와 같은 대형 몬스터의 가죽보다 단단한 피부와 살도 이번만큼은 소용없었다.

만년한철로 이루어진 백염의 창날은 목표를 관통하는 것으로도 모자라 땅 깊숙이 처박혔고, 진태경은 작살에 꿰인 물고기처럼 퍼덕이는 놈을 뒤로한 채 지면을 박찼다.

오직 그에게만 허락된 이능(異能)을 발휘하며.

‘인벤토리 오픈, 소환. 소환. 소환.’

쉬쉬쉬쉭!

빛살처럼 허공을 가로지르는 십여 개의 비수.

어느덧 유일하게 두 발로 서 있던 네임드 몬스터가 막강한 마력이 넘실대는 검을 휘둘러 비수들을 모조리 쳐냈을 때는, 이미 모든 것이 늦어 있었다.

스륵.

유령환살보(幽靈幻殺步)의 묘리가 담긴 움직임으로 적의 품속 깊숙이 파고든 진태경이, 끝끝내 손에 쥐고 있던 마지막 비수를 휘둘렀다.

나지막한 한 마디와 함께.

“더럽게 단단하긴 한데.”

서걱!

“그게 강하다는 뜻은 아니지.”

쿵.

그리고 이 미터가 훌쩍 넘어가는 거구가 힘없이 허물어진 그 순간.

구구구구궁.

돌연 공간을 뒤흔드는 거대한 울림과 함께, 휘황한 섬광이 모두의 머리 위로 드리워졌다.



* * *



무림으로 떠나 있었던 지난 몇 달 동안 얻은 깨달음 덕분일까.

나는 그 누구보다 먼저 기시감을 느꼈고, 동시에 높은 허공 위에서 불현듯 드리워지는 거대한 기운의 존재를 깨달았다.

‘빌어먹을, 또?’

당연하다면 당연하겠지만, 지금 이 상황에서 가장 먼저 든 생각은 예상치 못한 또 다른 적의 등장이었다.

내가 쓰러트린, 그리고 아직 스켈레톤 킹과 접전을 벌이고 있는 정체불명의 네임드 몬스터들과 같은 강력한 존재의 출현.

아마도 그 때문일 것이다.

그 강렬한 울림이 하늘을 떨어 울림과 동시에, 지상에 서 있던 모두의 움직임이 멈춘 것은.

하지만 어째서일까.

순간 벼락처럼 머릿속을 스쳐 지나간 불길한 예상과는 달리, 매번 내 본능이 울리던 붉은색 경고등은 허공을 집어삼키는 섬광 앞에서도 잠잠했다.

아니. 오히려 그 섬광이 크게 부풀어 오를수록, 내 마음 역시 평온해졌다.

이제 막 두 번째 네임드 몬스터를 쓰러트리고, 마지막 적과 사투를 이어 가고 있던 스켈레톤 킹은 아니었지만.

“어? 어어?”

쓰나미를 동반한 진도 8.0의 강도 높은 동공 지진.

점마 저거 뭐고, 하는 표정으로 하늘을 힐끔거리던 녀석이 멀뚱히 서 있는 나를 향해 다급히 외쳤다.

“뭐 해! 구경만 하지 말고 손 좀 써봐!”

“알겠어.”

순순히 대답한 나는 양손을 번쩍 치켜들고 흔들었다.

허공을 향해서.

“뭐해! 이 개자식아!”

“인사.”

“……뭐?”

친절한 설명에도 쉽게 이해하지 못하는 녀석을 향해, 나는 씩 웃어 보였다.

“먼 길 온 사람한테, 인사 정도는 해 줘야지.”

“그게 무슨 헛소……!”

더 이상 참지 못한 스켈레톤 킹이 버럭 외친 바로 그 순간.

파아아앗!

허공에 응집하던 빛무리가 폭발했다.

그리고 사방을 뒤덮은 그 아득한 섬광 속에서, 돌연 조금 전과는 다른 파괴적인 기운이 들끓었다.

쉬이이이잉!

나는 더욱 크게 두 팔을 벌렸다.

거센 파공성과 함께 벼락처럼, 화살처럼 오직 몬스터들을 향해 쏟아져 내리는 무수한 빛줄기들을 향해.

이 모든 것을 불러일으킨, 내 친구이자 어느 위대한 대마도사를 향해.
```

## Final English reading copy

```markdown
# Chapter 1148

For a martial artist, an increase in martial prowess meant more than heightened senses. It was directly tied to concentration, too.

No matter what happened around him, he could pour out everything he had in a single instant, with a terrifying focus that allowed only one thought.

That was Jin Taekyung now.

Ding.

A familiar chime pierced his ears.

But his senses had been sharpened to the edge of a blade forged by a renowned master. They hadn’t dulled in the slightest.

If anything, they’d grown even sharper.

*What was that?*

The sudden appearance of the mysterious named monsters.

He’d already killed one of them, but before any satisfaction came the heavy sensation transmitted through his spear and an inexplicable wariness. That wariness soon turned into even faster movement.

Flash.

A perfect Shifting Form and Position, leaving not even an afterimage.

Six bolts of magical power shot after him a beat too late and passed harmlessly through empty air. At the same time, White Flame in Jin Taekyung’s hands once again spewed fire.

Fwoosh—KABOOM!

Space warped along the spearhead’s slanting downward arc. Deep-blue flames, carrying a tremendous amount of Scorching Yang Qi, sliced through another named monster.

Or, rather, it looked that way.

At least, until Jin Taekyung felt the powerful recoil through the spearhead.

CRUNCH!

“……!”

Jin Taekyung stared wide-eyed at the named monster hurled far into the distance.

And at the same time, he understood the source of the inexplicable wariness he’d felt when he killed the first one.

*They’re tough.*

He wasn’t talking about their movements or their aura. Quite literally, their bodies were damn tough.

So tough that even he, who had brought down countless enemies, could hardly make sense of it.

*They’re so tough White Flame can’t cut all the way through?*

What kind of weapon was White Flame?

A ridiculously overpowered item of the kind he’d never have even seen if the System hadn’t showered him with all sorts of rewards early on—and a priceless treasure that no amount of money in Murim could buy.

Even the modern world’s artifacts, decked out with cutting-edge technology and all kinds of Magic, couldn’t match White Flame’s natural sharpness and durability.

And yet the monsters’ bodies—especially their bones, which were far denser than he could have imagined—couldn’t be cut like tofu, even by White Flame’s spearhead, wreathed in Force.

Sure, the monster had suffered a horrific wound in exchange. But the fact that it still stood, when it should have been split cleanly in two from collarbone to pelvis, was a shock to Jin Taekyung.

Its incredible regenerative ability, already restoring the wound in an instant, was just a bonus.

“How is this even possible?”

A question slipped from his lips before he knew it. The Skeleton King, who had joined him by now, answered.

“I thought the same thing at first. But when I thought about it, it wasn’t impossible to understand.”

“Why not?”

“If a human as monstrous as you can exist, why can’t monsters like them?”

“Are you kidding? I’m an exception.”

“Do you have to say things that put me off my food like it’s nothing?”

“Food? You’ve really become Korean. Weren’t you supposed to be playing a foreigner?”

The question had been based on reasonable evidence, but Mr. Stone King, from Atlanta, Georgia, had just learned a lot from a marvel of civilization called a smartphone.

“I’m Korean American.”

“……Your way with words has gotten pretty good since I last saw you.”

“Who knows? It’s not the only thing that’s improved.”

WHOOOOSH.

The moment he finished speaking, a tremendous mass of magical power swelled around him.

Jin Taekyung blinked silently at the stark difference in power from before. The Skeleton King shrugged.

“What, are you trembling at my might?”

“……What the hell happened while I was gone?”

“A lot. But there’s no time to tell you about it now.”

The Skeleton King had a clear-eyed grasp of reality.

Not far away, Choi Minwoo was leading the Hunters in a fierce battle against the monsters. The six named monsters had formed a semicircle around them.

Ssshhh.

Materialized magical power rippled like fog.

Behind the skull masks covering their entire faces, their gazes—devoid of even a hint of emotion—stabbed at the two of them like blades.

“Go for the neck. It’s the easiest part to cut.”

At the Skeleton King’s advice, his back now pressed against Jin Taekyung’s, Jin adjusted his grip on the spear and replied.

“I know.”

“We’ll take half each. Three for me, three for you.”

“Can you handle that? You’re weak as hell.”

“Arrogant human. Have you got a knife embedded in your tongue?”

Just then, the Skeleton King stopped grumbling. Then, in a voice so quiet it was almost inaudible, he added:

“Still… it’s good to see you.”

“What was that?”

“I said I’m damn glad to see you again, even if it had to be like this.”

Jin Taekyung wondered what he should say, then simply let out a soft laugh.

Before an awkward silence could settle between them, he pushed off the ground and charged at the enemies.

Just as his monster friend had done, he answered in a very quiet voice.

“Yeah. Me too.”

It all happened almost at once.

The wind rushing over his whole body swallowed his voice.

Jin Taekyung’s form, launched faster than sound, reached the monsters a step ahead of the Skeleton King.

KABOOM!

Three swords clashed with one spearhead, and a deafening roar erupted.

But this wasn’t an even match. The monsters, unable to withstand his power, were driven back, while Jin Taekyung kept advancing.

KABOOM! KABOOM! CRUNCH!

Amid the successive crashes, one named monster couldn’t keep up with Jin Taekyung’s strength and speed and dropped to its knees. He didn’t hesitate.

Slash!

The heavy sensation traveled through the spearhead.

With a strike even stronger than usual, the head wearing a pure-white skull mask floated into the air.

Two swords were already swinging at him from either side, but the attacks came half a beat too late to reach Jin Taekyung.

No—instead, the punch he threw after them struck empty air first.

WHUMP!

Compressed air exploded.

Like striking a mountain to hit the cow behind it, the shock wave burst out in an instant, driving the monsters back and opening a gap.

A tiny opening, but one that could decide the difference between life and death.

Whoosh!

The sequence of movements didn’t need so much as a preparatory motion.

Drawing on physical abilities that made even the word *superhuman* woefully inadequate, Jin Taekyung threw his spear.

THUNK!

The spearhead shot through the air as if plunging down from above, piercing another named monster’s body.

Just as its owner intended, it slipped precisely between its bones.

CRUNCH!

Its skin and flesh, tougher than those of a giant monster like an ogre, were useless this time.

White Flame’s spearhead, forged from Ten-Thousand-Year Cold Iron, did more than pierce its target. It drove deep into the ground. Jin Taekyung left the monster writhing like a fish caught on a harpoon and pushed off the ground.

He unleashed the ability granted to him alone.

*Inventory open. Summon. Summon. Summon.*

Whoosh, whoosh, whoosh!

A dozen or so daggers streaked through the air like beams of light.

By the time the only named monster still standing on two feet swung its sword, brimming with tremendous magical power, and knocked away every dagger, it was already too late.

Slip.

With a movement infused with the subtle principles of Ghost Illusory Slaughter Step, Jin Taekyung plunged deep into the enemy’s reach and swung the last dagger still in his hand.

He spoke in a low voice.

“You’re damn tough, but…”

Slash!

“That doesn’t mean you’re strong.”

THUD.

And just as the towering figure, well over two meters tall, crumpled limply to the ground—

Rumble.

A vast tremor suddenly shook space, and a dazzling flash fell over everyone’s heads.

* * *

Maybe it was thanks to the enlightenment I’d gained over the past few months away in Murim.

I felt a sense of déjà vu before anyone else, and at the same time became aware of a tremendous presence suddenly looming high overhead.

*Shit, again?*

Perhaps it was only natural, but the first thing that came to mind in this situation was the arrival of yet another unexpected enemy.

Another powerful being like the mysterious named monsters I’d taken down—and the ones the Skeleton King was still fighting.

Maybe that was why everyone on the ground froze as the powerful rumbling shook the sky.

But why?

A foreboding prediction flashed through my mind like lightning, yet the red warning light that always blared with my instincts stayed quiet, even as the flash swallowed the sky.

No. The larger the flash grew, the calmer I felt.

The Skeleton King, who had just taken down a second named monster and was fighting desperately against the last enemy, didn’t feel the same way.

“Uh? Uh, hey!”

His pupils were shaking like an earthquake measuring 8.0, complete with a tsunami.

He glanced up at the sky with a look that said, *What the hell is that?* Then he shouted at me, standing stock-still.

“What are you doing? Quit gawking and do something!”

“Okay.”

I obediently raised both hands and waved.

At the sky.

“What are you doing, you bastard?!”

“Waving hello.”

“……What?”

He clearly couldn’t understand, despite my helpful explanation. I gave him a grin.

“Someone came a long way to get here. The least we can do is say hello.”

“What the hell are you—”

The Skeleton King could hold it in no longer. He burst out in anger—

And at that very moment—

FLASH!

The light gathering in the sky exploded.

And amid the distant flash that covered everything around us, a different, destructive energy suddenly surged.

WHOOOOOSH!

I spread my arms even wider.

Toward the countless streaks of light raining down like lightning, like arrows, accompanied by a fierce whistle—and aimed only at the monsters.

Toward the one who had set all of this in motion: my friend, a great Grand Mage.
```
