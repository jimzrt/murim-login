<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1162.txt",
      "sha256": "0a53ed8a3061c43bd5065698e92cd03b15a1e36c1a8074916e01fc3bffea9ce3",
      "bytes": 12912
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2dac1019bff59404059c953e7e6c7080cca20532aa1c6178a30f782e4dda380d",
      "bytes": 1525
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2fd0de0ff721805936794bca4b9ad70fd4d20f40fbc76e97c8e8c5be179dfa5d",
      "bytes": 247561
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "97bcfa6b023b61aade5de5161ad86de92cc2033da35d5becb58fd381bcb81a2e",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9a01b9a9b604b91aeac7f65a6bfe177f882428dc4b081ac29f1a2fcf42b5cec1",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e5822e618691f47eddf4d8f558417cb71758ce480593bbc567c277f4e4a14546",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b6b8537f2453fa41498ad80ca19d95411ff76465857dc94cf644f36eb8e744c5",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "9a100b87fcd05206b1a5a6adcc284f131d4b3533c191c42c6c42424ebeb845d0",
      "bytes": 768
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2b956b1c2b1622350abdc3ded664fb5fb193ea44909588875f52f5f3a1d32384",
      "bytes": 294061
    }
  ],
  "estimated_tokens": 9548
}
-->

# Durable State Update — Chapter 1162

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
1 and safe_through 1162. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1162. Profile updates may replace only one
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
  "chapter": 1162,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1162,
    "continuity_sources": [1162],
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
    "Morgoth's three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "The World Hunter Federation was ordered to mobilize for Moscow against Morgoth and his monsters; Jin intended to go alone.",
    "The Skeleton King survived the Dragon Lair's blast but is unconscious and reduced to his head; Morgoth survived with a wound through his palm from the Hero's Sword.",
    "The Skeleton King rejects Morgoth's claim over him and names Jin Taekyung as his friend.",
    "Morgoth is newly curious about Jin Taekyung and friendship; an unidentified guest has arrived while Morgoth holds the Hero's Sword.",
    "Morgoth was summoned by Asmodeus from beyond distant stars and space, but says he is not devoted to Asmodeus."
  ],
  "continuity_sources": [
    1161
  ],
  "open_questions": [
    "Who is the unexpected guest, and what does the guest mean by asking what Morgoth is holding?",
    "Will the Skeleton King recover from the blast?",
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "What will happen when Morgoth's three-day deadline expires?"
  ],
  "safe_through": 1161,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 화산     | **Huashan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 흑마법사 | **black wizard** | Ruler or magical classification associated with the Gate. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 구천 | **Nine Springs** | Euphemism for the realm of the dead. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 골골 | 진태경 | subordinate_undead_to_captor_and_master | human | mocking, reluctant, and familiar | Calls Jin 인간 and 간악한 인간 while complaining about being deceived into searching Area A. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1161
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1161
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1161
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1161
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1161
- **Aliases:** None
- **Role:** Morgoth is a Dragon and the sovereign of a vast palace who seeks to recruit the Skeleton King as his Guardian.
- **Personality:** Composed and intellectually curious, he pursues the unknown with consuming greed and will abandon restraint when confronted with something unprecedented.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth offers the Skeleton King the role of Guardian, which the Skeleton King refuses.

## Korean source

```text
＃1162화



일순간, 세상이 멈춘 듯했다.

흐릿하게 주위를 감싸안은 마력의 안개도, 산처럼 쌓인 몬스터들의 사체와 살아남은 괴물들이 내지르고 있는 괴성도.

내 주위를 둘러싸고 있던 모든 것이 지워졌다.

더는 느껴지지도, 보이지도 않았다.

오직 단 하나.

저 멀리 칠흑색 머리카락을 망토처럼 늘어트린 어느 사내와 그의 손에 들린 새하얀 백골만이 망막에 틀어박힐 뿐이었다.

마치 이 세상에 존재하는 유일한 것처럼.

심장이 쥐어짜여지는 듯한 고통을 동반하며.

“지금, 손에 들고 있는 게 뭐지?”

억눌린 목소리가 백여 미터의 거리를 넘어 흘러가고, 그 끝에는 나를 물끄러미 바라보고 있는 사내가 있다.

아니, 인간의 거죽을 뒤집어쓴 한 마리의 사악한 흑룡(黑龍)이.

“아, 이것 말인가.”

이 세상의 것이 아닌 것 같은 아름다움과 너무나도 순수하기에 더욱 끔찍하게 느껴지는 악의가 놈의 입술 사이로 흘러나온다.

“내 오랜 갈망을 해결해 줄 실마리이자, 매우 값진 전리품이지.”

입꼬리를 비스듬히 말아 올리며, 모르고스가 덧붙였다.

“누군가의 친구일 수도 있고.”

“……!”

“인간과 몬스터의 우정이라. 감명 깊은 이야기더군. 이렇게 자네가 홀로 나타난 것을 보아하니 전부 사실이었던 모양이야.”

나는 모른다.

이곳에서 정확히 무슨 일이 벌어졌는지.

또 어떤 이야기가 오갔는지.

하지만 한 가지만은 확신할 수 있었다.

스켈레톤 킹은 최선을 다했으며, 그것은 분명 나와 우리 모두를 위한 마음에서 비롯되었으리라는 것을.

그렇기에 가장 중요한 것을 묻지 못했고, 흑요석 같은 두 눈동자는 그런 내 모습을 빠짐없이 응시하고 있었다.

“두려운가?”

마음을 읽어 낸 듯한 물음에, 나는 짤막하게 대꾸했다.

“그래.”

“무엇 때문에?”

“지금 내 앞에는 정신 나간 드래곤 한 마리가 있고, 그놈은 내가 아주 잘 아는 누군가를 붙잡고 있거든. 그리고 난 그 녀석이 아직 살아 있기를 바라고.”

망설임 없이 쏟아낸 대답 때문일까. 잠시 침묵하던 모르고스가 피식 웃었다.

“솔직한걸. 당황스러울 정도로.”

“그래서, 대답은?”

“앞서 말하지 않았나. 값진 전리품이라고. 워낙 난폭하게 날뛰는 바람에 약간의 흠집은 났지만, 그렇다고 산산조각 나는 건 내가 원치 않아.”

그 말에 담긴 의미는 명백했다.

그래. 아직 살아 있다.

녀석이, 스켈레톤 킹이.

이 빌어먹을 폐허에 발을 디딘 그 순간부터, 간절히 기다려 왔던 대답.

그제야 참았던 숨을 토해 낸 나는 진심을 실어 말했다.

“고맙다. 이 개자식아.”

“별말씀을. 오랜만에 찾아온 귀중한 기회를 놓칠 수야 있나.”

“인질극 하는 취미는 없겠지?”

“인질극이라, 그런 싸구려 유희를 즐기기에는 내 지성과 격이 너무나도 높지.”

“그거 듣던 중 반가운 소리군.”

“글쎄, 달리 생각해 본다면 무엇보다 나쁜 소식일 수도 있다네. 나는 전리품과 그 외의 것을 확실히 구분 짓는 편이거든.”

“구분?”

“만약 소유할 수 없을 만큼 위험한 것이라면, 반드시 부숴야만 하지. 그래야 아무런 뒤탈이 없으니까.”

모르고스의 입가에 맺혀 있던 미소가 한층 짙어졌다.

“바로 자네처럼.”

그 순간.

스아아아아.

일대를 휘감은 마력이 소용돌이쳤다.

믿을 수 없이 순수하고, 거대한 힘의 파도가.

그리고 마치 손에 닿을 듯이 선명하게 느껴지는 살의(殺意)가.

“처음부터 이럴 생각이었나?”

“아니, 하지만 처음 마주한 순간 깨달았지. 나 역시 과거의 아스모데우스와 같은 실수를 저지를 수도 있겠다는 것을. 그리고 무엇보다…….”

흥미와 아쉬움이 뒤섞인 불쾌한 시선이, 내 전신을 꿰뚫어 보듯 응시했다.

“사냥감.”

바닥에 닿을 만큼 긴 머리카락이 허공으로 부유한다.

마치 신화 속에 등장하는 존재의 날개처럼.

동시에 천사가 아닌 악마의 그것처럼.

“자네는 나를 이미 사냥감으로 보고 있지 않나. 진태경, 젊고 강인한 인간 영웅이여.”

일순간 흐르는 적막 사이로, 나는 입을 열었다.

“그래, 맞아.”

헌터(Hunter). 인류를 수호하는 검이자 방패이며, 사냥꾼.

그러나 놈과 정면으로 맞서고자 한 이유는 단지 그뿐만이 아니다.

만약 모르고스가 정말로 믿을 수 있는 존재였다면, 나는 기꺼이 그가 원하는 대로 했을 것이다.

엎드려 절을 할 수도 있고, 스스로 팔다리를 자르라 해도 기꺼이 따랐을 것이다.

목숨?

나와 천태민, 두 사람의 죽음으로 수십억 인류가 평화를 얻는다면 두말없이 내놓을 수 있었다.

그것이야말로 내 의무니까.

하지만 앞서 모르고스가 그랬듯, 나 역시 놈을 마주한 그 순간 명확하게 깨달았다.

눈빛.

투명하리만치 순수한 저 눈빛이, 한여름 낮 아스팔트 바닥을 기어가는 개미를 구경하는 어린아이의 그것과 다르지 않음을.

그랬기에, 수천만이 넘는 목숨이 가루가 되어 사라졌다.

지금 내가 발을 딛고 서 있는, 바로 이 자리에서만.

그리고.

한 가지 더.

“전리품이 아니야.”

“뭐?”

“전리품 따위가 아니라고. 그 녀석은.”

남의 것처럼 낯선, 들끓는 음성과 함께 걸음을 옮겼다.

천천히. 동시에 무겁게.

그리고 그 어느 때보다 힘주어 내디딘 발걸음을 따라, 어제 일처럼 생생한 기억들이 자국보다 깊게 새겨졌다.

저벅.



‘인간이여, 그러지 말고 나와 거래를 하는 것이 어떻겠나?’

‘거래?’



그래, 그곳이었다.

A급 게이트, 흑마법사의 검은 숲.

죽은 나무가 우거진 그 어두컴컴하고 축축한 숲에서 우리는 처음 만났고, 그렇게 함께하게 됐다.

처음 생각했던 것보다도, 아주 오랜 시간을.

저벅.



‘야. 워로드 몬.’

‘그 따위 이름으로 부르지 마라. 이 몸은 검은 숲의 주인이자 위대한 언데드 군단의 사령관이다.’

‘흠. 좋아.’

‘드디어 말이 통하는군.’

‘그래서, 골골아.’

‘……이런 제기랄.’



정확히 언제부터였는지 모르겠다.

녀석을 단순한 몬스터가 아닌, 그 이상의 존재로 받아들이기 시작했던 게.



‘무슨 일 있냐? 아까부터 왜 이렇게 축 쳐져 있어?’

‘그냥, 문득 그런 생각이 들었다.’

‘무슨 생각?’

‘과거의 나는, 과연 어떤 존재였을까.’



그날, 고뇌에 빠진 녀석에게 나는 말했었다. 잘은 모르겠지만, 분명 썩 괜찮은 놈이었을 거라고.

그리고 괜한 쑥스러움에 혼잣말하듯 흘려보낸 그 한마디를, 녀석은 잊지 않았다.



‘인간, 궁금한 것이 있다.’



시간이 흐른 지금에도 눈앞에 선명히 떠오른다.

움직일 수 없을 만큼 지치고 다친 내게 아크 리치가 쏘아 보낸 백염의 창날이.

스스로의 힘으로 인벤토리에서 빠져나와 온 몸으로 나를 막아선 녀석의 모습과.



‘도대체…… 왜?’

‘인간. 궁금한 것이 있다.’



마지막인 줄만 알았던 그 목소리가.



‘지난번에 내게 했던 말, 진심이었나?’

‘당연히, 진심이었지.’



내 대답을 듣고 나서야 초승달처럼 휘어지던 그 흐릿한 안광이.



‘그래. 그렇군.’



그렇게 검은 숲에서 처음 만난 스켈레톤 워로드는 쓰러졌고.



‘도대체 왜, 라고 물었었지.’



인간들의 땅 위에서, 인간을 지키기 위해 희생한 새로운 존재가 빛나는 왕관과 함께 다시 일어났다.

언젠가 내가 해 주었던, 누군가에게는 영원히 잊지 못할 그 한 마디를 되돌려주며.



‘넌 간악하지만, 썩 괜찮은 인간이니까. 단지 그뿐이다.’



스켈레톤 킹.

구천을 떠도는 망자들의 주인이자 왕.

그리고…….

‘내 친구.’

뜨겁다.

오직 모르고스만을 직시하고 있는 눈동자도.

긴 기다림 끝에 폭발한 활화산처럼, 쉼없이 열양지기를 뿜어내고 있는 두 개의 단전도.

마지막으로, 앞서 스쳐 간 그 모든 기억을 담아 내디딘 발걸음도.

콰득.

깊게 퍼져나가는 울림.

초토화된 지면이 다시금 으스러진다.

거미줄 같은 실금이 사방으로 번지고, 이내 폭발한다.

화륵, 콰아아앙!

염화일로(炎火一路).

한 줄기의 맹렬한 화염이 되어, 나는 쏘아졌다.



* * *



그야말로, 한순간이었다.

콰아아!

불현듯 피어오른 검푸른 불꽃과 함께, 두 존재 사이에 놓여 있던 백여 미터의 공간이 단숨에 사라졌다.

아니, 증발이라는 표현이 더 옳을지도 모른다.

그만큼 모르고스가 느낀 열기는 끔찍하리만치 강했고, 그 속도는 소리조차 앞지를 정도였으니.

하지만.

‘보인다.’

흑요석처럼 번뜩이는 흑룡의 두 눈동자는 그 모든 것을 읽고, 간파해 냈다.

어느덧 자신의 코앞까지 들이닥친 한 줄기의 불꽃과 그 거대한 열기 속에서 불현듯 모습을 드러낸 무언가를.

슈확!

“……!”

일순간 크게 뜨인 모르고스의 눈동자에, 비스듬히 내리그어지는 은빛 창날이 비쳤다.

도대체 저것은 어디서, 어떻게 나타난 것일까.

분명 그 어떤 마법의 힘도 느끼지 못했는데.

하지만 의문에 대한 답을 찾기도 전에, 창날에 실린 화염이 먼저 그의 가슴을 파고들었다.

아니, 그렇게 보였다.

아주 잠깐 동안은.

팟, 서걱!

찰나를 쪼개고 쪼갠 순간, 단숨에 공간을 뛰어넘은 모르고스는 말없이 손을 들어 자신의 가슴 어림을 매만졌다.

정확히는 단지 스친 것만으로도 까맣게 타들어 간 살갗의 일부를.

“……뜨겁군.”

수천 년을 세월을 살아오며 세 번째로 느껴 보는 통증.

그러나 그에게 두 번째 고통을 안겨 주었던 어느 언데드 몬스터와는 달리, 저 멀리 창날을 늘어트린 채 다가오고 있는 인간은 아직도 거대한 힘을 간직하고 있었다.

모르고스가 순수한 의문을 담아 물어볼 정도로.

“혹시, 동족인가?”

천천히, 그러나 신중하게 거리를 좁히며 진태경이 담담하게 대답했다.

“그래, 오랜만이다. 아들.”

“천박한 언행을 보니 동족이 아닌 것은 확실한데…… 인간이라면 어떻게 그리 빠르게 강해질 수 있는 거지?”

모르고스는 이미 진태경에 대해 알고 있었다. 그것도 아주 자세하게.

그리고 모르고스가 이 세상으로 소환되기 전까지만 하더라도, 진태경이 보여 준 힘은 결코 이 정도가 아니었다.

“많은 일이 있었지. 너 같은 놈도 도저히 상상할 수 없는, 그런 일들이.”

“……나조차도 상상할 수 없는 일이라.”

어찌 이토록 매혹적일 수 있을까.

하지만 마음 깊은 한구석에서 불쑥 고개를 드는 호기심을 모르고스는 애써 억눌러야 했다.

한순간의 호기심에 휩쓸리기에는, 눈앞의 인간은 충분히 위험한 존재였으니까.

“아쉽지만, 자네의 그 흥미로운 이야기는 앞으로도 영원히 듣지 못하게 되겠군.”

낮은 뇌까림과 함께, 모르고스는 갈퀴처럼 그러쥔 두 손으로 허공을 움켜쥐었다.

아니, 찢었다.

그그그그극.

일그러진 공간이 아가리를 벌리고, 어둠만이 일렁이는 그 틈새 너머로 지금껏 드러나지 않았던 존재들이 모습을 나타냈다.

철컥, 철컥.

예리한 창칼과 전신을 빈틈없이 보호하는 갑주.

수백을 넘어 수천에 달하는 그들은 마치 같은 배에서 태어난 쌍둥이처럼 서로를 닮아 있었고, 진태경은 자신이 이 세상으로 귀환한 첫날의 기억을 떠올렸다.

“저건…….”

“나의 가장 충직한 수호자들이지.”

용아병(龍牙兵).

드래곤에 의해 탄생하고, 오직 드래곤을 위해 존재하는 가디언.

하지만, 진태경을 얼어붙게 한 것은 단지 그뿐만이 아니었다.

“……파이 첸?”

용아병들 사이로 보이는 낯익은 얼굴에, 나직한 신음이 그의 입술 사이로 흘러나왔다.
```

## Final English reading copy

```markdown
# Chapter 1162

For an instant, it was as if the world had stopped.

The haze of magical power faintly wrapping around the surroundings. The monsters’ corpses piled up like mountains, and the surviving monsters’ roars.

Everything around me vanished.

I could no longer feel or see any of it.

There was only one thing.

Far away, a man with pitch-black hair hanging down like a cloak, and the pure-white skeleton in his hand, burned into my retinas.

As if they were the only things in the world.

Pain clenched my heart.

“What are you holding in your hand?”

My restrained voice crossed the hundred or so meters between us. At the other end stood a man gazing at me in silence.

No—a wicked Black Dragon wearing human skin.

“Ah. This?”

A beauty that seemed to belong to another world, and an evil so pure it was all the more horrifying, spilled from his lips.

“A clue that may satisfy my long-held desire, and a very valuable trophy.”

Morgoth added, one corner of his mouth curling upward.

“Perhaps someone’s friend, too.”

“……!”

“The friendship between a human and a monster. It was a moving story. Judging by the fact that you came here alone, it seems it was all true.”

I didn’t know.

I didn’t know exactly what had happened here.

Or what had been said.

But I was certain of one thing.

The Skeleton King had done everything he could, and he had done it for me—for all of us.

That was why I couldn’t ask the most important question. His obsidian eyes watched me closely, taking in every part of me.

“Are you afraid?”

As if he’d read my mind, he asked. I gave him a brief answer.

“Yeah.”

“Of what?”

“There’s a crazy Dragon standing in front of me, and he’s holding someone I know very well. I want that guy to still be alive.”

Maybe it was my unhesitating answer. After a brief silence, Morgoth gave a quiet laugh.

“You’re honest. Almost disconcertingly so.”

“So, your answer?”

“Didn’t I already tell you? A valuable trophy. He was so violent in his rampage that he’s a little damaged, but I have no desire to see him shattered to pieces.”

The meaning behind those words was clear.

Right. He was still alive.

That bastard, the Skeleton King.

The answer I’d been desperately waiting for ever since setting foot in this godforsaken ruin.

Only then did I let out the breath I’d been holding. I put my whole heart into my words.

“Thanks, you son of a bitch.”

“Don’t mention it. I couldn’t pass up such a precious opportunity after all this time.”

“You don’t have a hobby of taking hostages, do you?”

“Hostage-taking? My intellect and stature are far too great for such a cheap amusement.”

“That’s good to hear.”

“Perhaps. Or perhaps it’s the worst news you could have heard. I make a clear distinction between trophies and everything else.”

“A distinction?”

“If something is too dangerous to possess, then it must be destroyed. That way, there won’t be any trouble later.”

Morgoth’s smile deepened.

“Just like you.”

At that moment—

*Vwoom.*

Magical power churned around us.

An unbelievably pure, colossal wave of power.

And a murderous intent so vivid it felt within reach.

“Were you planning this from the start?”

“No. But the moment we first met, I realized I might make the same mistake Asmodeus once did. And, more than anything…”

His unpleasant gaze, a mixture of interest and regret, pierced through me as if it could see right through my body.

“Prey.”

His hair, long enough to reach the ground, floated into the air.

Like the wings of a being from myth.

Except they belonged to a demon, not an angel.

“You already see me as prey, don’t you, Jin Taekyung? Young, strong human hero.”

Silence passed for an instant. I opened my mouth.

“Yeah. I do.”

A Hunter—the sword and shield that protects humanity, and a hunter.

But that wasn’t the only reason I intended to face him head-on.

If Morgoth had really been someone I could trust, I would have gladly done whatever he wanted.

I would have prostrated myself before him. If he’d told me to cut off my own arms and legs, I would have done it.

My life?

If the deaths of Cheon Taemin and me could bring peace to billions of people, I would have given them up without a second thought.

That was my duty.

But just as Morgoth had, I understood with absolute clarity the moment I faced him.

His eyes.

Those eyes, so clear they seemed pure, were no different from those of a child watching an ant crawl across the asphalt on a midsummer afternoon.

That was why tens of millions of lives had been ground to dust.

Right here, in the very place where I stood.

And one more thing.

“He’s not a trophy.”

“What?”

“He’s not some trophy. That guy.”

With a voice boiling over, strange enough to sound like someone else’s, I took a step.

Slowly. Heavily.

As my foot came down with more force than ever before, memories as vivid as yesterday sank deeper than its imprint.

*Thud.*

> “Human, instead of that, how about making a deal with me?”
>
> “A deal?”

Yeah. It was there.

A-rank Gate, the Black Forest of the Black Wizard.

We’d first met in that dark, damp forest thick with dead trees. And then we’d stayed together.

For far longer than I’d expected.

*Thud.*

> “Hey, Warlord Mon.”
>
> “Do not call me by such a name. I am the master of the Black Forest and commander of the mighty undead legion.”
>
> “Hmm. All right.”
>
> “At last, you understand.”
>
> “So, Bones.”
>
> “……Damn it.”

I couldn’t say exactly when it happened.

When I began to see him as more than just a monster.

> “Something wrong? Why’ve you been so down all day?”
>
> “I was just thinking about something.”
>
> “What?”
>
> “What kind of being was I, in the past?”

That day, I’d told him as he brooded that I didn’t really know, but he’d probably been a pretty decent guy.

And he hadn’t forgotten the words I’d let slip as if talking to myself, embarrassed for no good reason.

> “Human, I have a question.”

Even now, the memory stood clear before my eyes.

The spearhead of White Flame, which the Arch Lich had sent flying at me when I was too exhausted and injured to move.

The Skeleton King forcing his way out of my Inventory by his own power and shielding me with his entire body.

> “Why…?”
>
> “Human. I have a question.”

The voice I’d thought I would never hear again.

> “What you said to me before—did you mean it?”
>
> “Of course I did.”

Only after hearing my answer did his dim ghostly eyes curve like a crescent moon.

> “I see.”

The Skeleton Warlord I’d first met in the Black Forest fell.

> “You asked why.”

Then, on human land, a new being who’d sacrificed himself to protect humans rose once more with a shining crown.

Returning the words I’d once said to him—the words someone would never forget.

> “You’re cunning, but you’re a pretty decent human. That’s all.”

The Skeleton King.

King and master of the dead who wander the Nine Springs.

And…

*My friend.*

I was burning up.

The eyes fixed solely on Morgoth.

The two dantians that, like a volcano erupting after a long wait, poured forth Scorching Yang Qi without pause.

And the step I took, carrying every memory that had just passed through me.

*Crack.*

A deep rumble spread.

The devastated ground crumbled again.

Hairline fractures spread in every direction like a spiderweb, then erupted.

*Fwoosh—KABOOM!*

Flamefire Path.

I shot forward as a single, blazing streak of fire.

* * *

It happened in an instant.

*BOOM!*

With a sudden flare of blue-black flames, the hundred or so meters between the two of them disappeared at once.

No—“vaporized” might have been more accurate.

The heat Morgoth felt was that horrifyingly intense, and the speed surpassed even sound.

But—

*I can see it.*

The Black Dragon’s obsidian eyes flashed as they read and saw through everything.

The streak of fire rushing up to his face—and something that suddenly emerged from within its immense heat.

*Whoosh!*

“……!”

Morgoth’s eyes flew wide. In them, a silver spearhead slashed down at an angle.

Where had it come from? How?

He hadn’t sensed the power of any magic.

But before he could find an answer, the flames riding the spearhead thrust into his chest.

Or so it seemed.

For the briefest moment.

*Tap. Slice!*

In a moment split into smaller moments, Morgoth crossed the distance in an instant. He silently raised a hand to touch the area around his chest.

More precisely, the patch of skin that had been scorched black by the slightest graze.

“……Hot.”

The third time in thousands of years that he’d felt pain.

But unlike the undead monster that had inflicted the second pain on him, the human approaching from afar with his spearhead lowered still held immense power.

Enough to make Morgoth ask with genuine curiosity:

“Are you, by any chance, one of my kind?”

Slowly but carefully closing the distance, Jin Taekyung answered calmly.

“Yeah. Long time no see, son.”

“Your vulgar speech makes it certain you’re not one of my kind…but how can a human grow so strong so quickly?”

Morgoth already knew about Jin Taekyung. He knew a great deal.

And until Morgoth had been summoned to this world, Jin Taekyung’s power had been nothing like this.

“A lot’s happened. Things even you couldn’t possibly imagine.”

“Things even I couldn’t imagine…”

How could it be so fascinating?

But Morgoth had to force down the curiosity that rose unexpectedly from deep within him.

The human before him was dangerous enough that he couldn’t afford to be swept away by a moment’s curiosity.

“I’m afraid I’ll never get to hear that interesting story of yours.”

With a low mutter, Morgoth clenched both hands like claws and grasped at empty air.

No—he tore it.

*Grrrrrrk.*

The warped space opened its jaws, and beyond the gap, where only darkness rippled, beings that had remained hidden until now emerged.

*Clank, clank.*

Sharp spears and blades. Armor covering them from head to toe without a gap.

They numbered in the thousands and resembled one another like twins born of the same womb, and Jin Taekyung recalled the first day he’d returned to this world.

“Those are…”

“My most loyal guardians.”

Dragon-tooth soldiers.

Guardians born of Dragons and existing only for Dragons.

But that wasn’t all that made Jin Taekyung go rigid.

“……Pai Chen?”

At the familiar face among the Dragon-tooth soldiers, a low groan slipped from his lips.
```
