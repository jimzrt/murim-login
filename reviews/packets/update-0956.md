<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0956.txt",
      "sha256": "4a82bcc69a53e1a72a0299b32b59fe3aa24b9caa5be0dbcbc65a39249751b030",
      "bytes": 13994
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bfe327195c73f5b756fd9a625dc5be094f725e20e456ff1050d5a05e1ab810f0",
      "bytes": 2233
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ebfc840d67104c97d0585f79795365156f1920a828fd6a4c5ba3dd3ca29b358d",
      "bytes": 234431
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "3cb6c728f9a3f10a9de00cd8b11d157f13314cf0c981e30ea5afd2e2b6fc3340",
      "bytes": 642
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "76ab8eee12cea0cb066e8d1d0ee4b546a0266a724bc4d577de346ecc350955ae",
      "bytes": 759
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "d28ea90c7c8af3b10c358cce8b6b08fb8f816064431e9177766536a160c3b2b8",
      "bytes": 568
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "010915462981eaa7991be99b3579ea5b68f8636265408ef698a078cda4fae09a",
      "bytes": 778
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4c18d32549b16773c0ae2f2444d6f37fab97b8d70e1c946594d215e90818110c",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "3080e893d300079ee0a65e3f49af7a6bbc4a783cec21cd329b3137febe3c8dfa",
      "bytes": 1119
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a20f593116af26c44513a62978f9565dd0243e9d8b9b1d44d682a18b3511712e",
      "bytes": 267908
    }
  ],
  "estimated_tokens": 10929
}
-->

# Durable State Update — Chapter 956

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
1 and safe_through 956. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 956. Profile updates may replace only one
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
  "chapter": 956,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 956,
    "continuity_sources": [956],
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
    "The steppe army has begun its assault on Eight Spring Gorge after the Jin forces devastated northern Shanxi’s fields, water sources, and homes and laid traps; the defenders’ battle remains unresolved.",
    "Jin Wikyung has promised his defenders they will celebrate the next Double Ninth Festival together on Mount Heng.",
    "Temur regrets ignoring the real Chinggen’s warnings and knows the man beside him is Chinggen’s killer and impostor, but conceals his knowledge.",
    "Jamukha leads the steppe army and has long awaited a call from “that person”; that person’s identity and purpose remain unknown.",
    "The Emperor remains gravely ill from Blood Soul Gu; the Divine Physician says saving him requires him to die once, and Taekyung’s quest to remove the Gu and treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha.",
    "After traveling without rest for seven days and nights, Taekyung is resting briefly with the Bow Saint and Jeok Cheongang; Taiyuan is about two days away.",
    "Taekyung resolves to trust his allies rather than try to bear every burden alone."
  ],
  "continuity_sources": [
    954,
    955
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge fare?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 955,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 천무학관   | **Heaven's Gate Temple**         |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 영약     | **elixir**                                       |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 운철 | **meteorite iron** | Material whose strength is used as a comparison for the black-wood fishing rod. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 철기당 | **Ironcraft Hall** | The Jin Family of Taiyuan hall led by Jang Taebo. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 텡그리 | **Tengri** | Deity invoked by the steppe people. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 장태보 | 항아 | elder_neighbor_to_child | Hanga | familiar and instructive | Calls the neighboring boy by name while correcting his speech and sending him home after dark. |
| 항아 | 장태보 | child_to_elder_neighbor | Grandpa | childlike-familiar | Repeatedly calls Jang Taebo 할부지. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 장태보 | Lesser_Family_Head_to_elder_smith | Old Master Jang | respectful and formal | Wikyung thanks Jang for coming. |
| 장태보 | 진위경 | elder_smith_to_Lesser_Family_Head | Lesser Family Head | respectful and deferential | Jang speaks with formal respect to Wikyung. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 954
- **Aliases:** None
- **Role:** The real Chinggen was a Khan of the eastern grasslands and Temur’s brother, but he was killed in the attack on their gathering; an impostor now wears his face.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; an impostor wearing Chinggen’s face now accompanies Jamukha and deceives Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 955
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 953
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** Jang Taebo is the former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths, now the Jin Family of Taiyuan’s Master of Ironcraft Hall.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 954
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 954
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and the people of Shanxi—including many commoners the Jin Family once aided—are willing to help defend their home alongside him.

## Korean source

```text
＃956화



팔천협(八天峽)은 백여 장 남짓의 길이로 이루어진 협곡이다.

삼십여 장에 달하는 아득한 높이의 암반으로 에워싸인 자연의 관문.

장정 서른 명이 간신히 어깨를 맞댈 정도로 좁은 폭을 지닌 탓에 공격하는 입장에서는 최악의 조건이었으나, 이 항아리 모양의 협곡에서 두 번에 걸쳐 산서성의 명운을 건 대전투가 벌어진 것은 그만한 이유가 있기 때문이다.

“뚫어라! 놈들을 짓밟고 나아가라!”

“대초원의 형제들이여, 이 빌어먹을 협곡만 넘어선다면 산서성은 우리의 것이 된다!”

팔천협은 산서성 일대에서 제일가는 전략적 요충지.

온통 험한 산지 이루어진 북부를 가장 신속하게 통과할 수 있는 지름길이자, 중부의 평야로 나아갈 수 있는 마지막 길목이기도 하다.

북부와 중부를 구분 짓는 경계에 위치한 이곳을 손에 넣는다면, 어깨를 나란히 한 채 지축을 뒤흔들며 달려 나가는 수만의 기마병을 막아설 장애물은 사라진다.

아니, 설령 있더라도 그저 짓밟으면 그만이다.

한낱 모래와 자갈로 파도를 막아 낼 수는 없는 법이니까.

하지만 바로 그렇기에, 방어자들 역시 무슨 수를 써서라도 눈앞의 침략자를 막아 내야 했다.

“버텨! 단 한 걸음도 물러서지 마라!”

“자랑스러운 산서인들이여! 잔인무도한 오랑캐로부터 고향 땅을 지켜라!”

“으아아아아!”

비명과도 같은 함성이 어둠을 뚫고 협곡을 떨어 울린다.

그리고 양측의 군대가 서로를 향해 쏘아 올린 빽빽한 화살비 속, 이 모든 상황에서 동떨어진 듯 홀로 유려하게 움직이는 한 줄기 섬광이 있었다.

쉭!

갈라지는 공간.

유목민 특유의 기성(奇聲)을 내지르며 달려들던 십여 기의 기마병은 불현듯 바람을 느꼈다.

단지 전신을 스쳐 지나가는 것이 아닌, 몸속 깊은 곳까지 훑으며 지나가는 서늘한 바람을.

“……어?”

동그랗게 뜬 눈. 동시에 흔들리는 시야.

그리고.

서걱.

두 번 다시 빛이 스며들지 않을, 영원한 암전(暗轉).

푸화악!

피분수가 허공으로 솟구친다. 한때 사람이며 말이었을 그것들이 조각조각 나뉘어 사방으로 튕겨 나갔다.

힘차게 달려오던 속도 그대로.

비록 살아서는 닿지 못한, 첫 목표로 삼았던 적을 향해.

콰드드득!

아무리 가벼워도 생전 수백 근, 천 근에 가까운 무게를 지녔던 인마(人馬)다.

흙과 피로 범벅이 된 채 깊은 고랑을 만들며 발치까지 밀려온 거대한 고깃덩어리들을, 진무경은 침착한 눈빛으로 내려다보았다.

정확히는 더할 나위 없이 깔끔한 그 절단면과, 자신의 손아귀에 들린 한 자루의 검을.

‘역시 예리하다. 믿을 수 없을 정도로.’

어둠 속에서도 서늘한 예기(銳氣)를 내뿜고 있는 검신을 바라보는 진무경의 눈에 감탄이 스쳤다.

불과 이틀 전, 일천의 적들을 상대로 나선 전투에서 새로운 검의 뛰어남을 한 차례 느꼈음에도 새삼 놀랍지 않을 수 없었다.

그 또한 명검에 대한 탐욕이 있는, 한 사람의 검수(劍手)였으니.

‘난데없이 처음 보는 검을 쥐여 주기에 무슨 일인가 했더니, 그때 거절했다면 두고두고 후회할 뻔했군.’

무림인에게 있어 애병(愛兵)이란 가장 가까운 친구이자 가족이다.

그러나 첫 출진을 앞두고 애검을 손질하던 진무경에게 찾아온 건장한 체구의 노인은, 대뜸 길쭉한 보자기를 내려놓더니 이렇게 말했다.



‘그건 버리고, 오늘부터는 이놈을 쓰시게. 일찍부터 이공자를 위해 벼려 둔 검이니.’



처음에는 정신 나간 늙은이라고 생각했다.

벌써 십 년을 넘게 써 온 애검을, 그것도 형님인 진위경이 태원진가의 기둥뿌리 하나를 뽑아 가면서까지 만든 명검을 버리라고 하다니.

하지만 곧이어 보자기 사이로 모습을 드러낸 한 자루의 검을, 마침내 검갑에서 알몸을 드러낸 그 새하얀 검신을 본 순간 진무경은 깨달았다.

눈앞의 정신 나간 늙은이는 난생처음 보는 뛰어난 장인이라는 사실을.

그것도 신병이기(神兵利器)를 벼려 낼 능력이 충분한.



‘얼굴을 보아하니 보는 눈은 있구먼. 다행이야, 그래도 주인이 될 자격은 있어 보이니.’

‘이건 도대체…….’

‘보면 모르나? 이 늙은이가 말년에 개고생해 가며 만든 최고의 역작 중 하나지. 만년한철(萬年寒鐵)과도 비견될 만한 것으로 벼려 냈으니, 부디 잘 다뤄 주시게.’



노인은 그 한마디를 남긴 채 망설임 없이 자리를 떠났고, 그 후에도 한참이나 새로운 검에 빠져 있던 진무경은 가솔로부터 노인의 정체를 들을 수 있었다.



‘그러고 보니 이공자께서는 모르실 수도 있겠군요. 본가에 철기당(鐵騎黨)이 새롭게 창설되었을 시기가 폐관 수련 기간과 겹치니까요.’

‘철기당? 그럼 아까 그 노인이…….’

‘예. 철기당의 수좌이신 장태보 당주십니다. 과거에는 삼십 년이 넘는 세월을 철기방(鐵騎房)의 방주로 지내셨지요.’

‘……!’



태원진가에서도, 천무학관에서도 언제나 무공 수련에만 매진했던 진무경도 철기방의 존재는 알고 있었다.

천하에서 내로라하는 장인들이 속한 곳.

설령 만금의 값을 치르더라도 자격이 되지 않는다면 결코 병장기를 팔지 않는다는, 그에 걸맞은 자부심과 실력을 지닌 집단.

그런 철기방에서 장장 수십 년이나 최고의 장인으로 군림했던 장태보가 왜 태원진가에 있는지는 가솔도 몰랐으나, 한 가지만큼은 확실히 알고 있었다.



‘삼 공자님과 인연을 맺으신 것으로 압니다. 하여 이공자님께서 폐관에 들어가실 무렵, 은퇴를 번복하시고 본가에 몸담게 되셨지요.’

‘태경이, 그 녀석과?’

‘예. 그리고 그 과정에서 장 당주께서 무슨 수를 쓰셨는지, 철기방에 속해 있었던 장인들도 대거 데려오셨습니다. 아마 과거의 인연 때문이겠지요.’



하지만 그 정보를 알려 준 가솔도, 이제 막 폐관을 끝마친 진무경도 까맣게 모르는 사실이 있었다.

모든 것을 내팽개치고 태원진가로 달려온 장인들은 결코 의리 따위로 움직이지 않는다는 것을.

장태보보다도 앞서 대장간을 떠났던 늙은 명장(名匠)들마저 돌아오게 한 것은, 만 리가 넘게 떨어진 어느 깊은 강물에서 헤엄치던 거대한 영물(靈物)이 남긴 마지막 선물이라는 것을.

수신룡(水神龍).

여의주를 얻지 못한 이무기는 끝끝내 용이 되지 못하고 암천에 의해 타락했으나, 한 청년의 도움으로 영원한 안식을 얻어 자신의 신령스러운 육신을 남겼다.

그 어떤 이름난 장인이라 해도 이성을 상실할 수밖에 없는, 어쩌면 하늘에서 떨어진 운철(隕鐵)이나 만년한철보다도 희귀한 연마 재료를.

그리고 한편으로는 당연하게도, 그중 상당수는 비밀리에 태원진가로 흘러들어왔다.

수백 년에 걸쳐 영력을 머금은 살점과 피는 그 자체로 영약이 되었고, 엄청난 강도를 지닌 뼈는 병장기로 탄생했으며, 크고 단단한 힘줄과 근육은 갑옷의 일부가 되었다.

그렇게 수신룡의 일부는, 어느덧 태원진가 곳곳에 녹아들어 있었다.

바로 지금 이 순간처럼.

쐐애애액!

제아무리 그물이 촘촘하다 한들, 송사리까지 어찌할까.

진무경 단 한 사람을 뚫지 못해 막혀 버린 상황 속.

처참한 죽음을 맞이한 동료의 모습에 주춤하던 유목민들이 견제를 위해 쏘아 보낸 화살은, 관군들의 방패 사이를 스쳐 태원진가 무인의 가슴에 틀어박혔다.

아니, 적어도 그 순간만큼은 그렇게 보였다.

텅!

앞서 울려 퍼진 강맹한 파공성이 무색하리만치 힘없이 튕겨 나가는 화살.

치명상을 직감하고 비명을 지르려던 태원진가 무인이 눈을 동그랗게 떴다.

“커허헉…… 응?”

멍하니 눈을 깜빡이던 그는 마침내 기억해 냈다.

소가주의 엄명에 따라 무복 뒤 가슴팍에 덧대두었던 얇은 무언가를.

철판인지 가죽인지 구분이 안 될 만큼 가볍고, 묘한 빛이 감도는 그것을.

그리고 기억을 떠올림과 동시에, 언제 그랬냐는 듯 크게 소리 내어 웃었다.

“이 등신 같은 오랑캐 새끼들아! 그렇게 쏴서 우리 집 개라도 맞출 수 있겠느냐!”

“……!”

“……!”

당장이라도 나약한 한족 놈들을 짓밟을 생각이었던 유목민들은 당혹스러운 표정으로 서로를 바라볼 수밖에 없었다.

어지간한 가죽 갑옷쯤은 가볍게 꿰뚫는 힘을 지닌 활이 무용지물이라니.

초원을 상징하는 가장 강력한 무기 중 하나가 사라졌다고 생각하자, 보이지 않는 동요가 번지는 것은 당연지사였다.

물론 그 찰나의 동요마저도 한낱 사치에 불과하다는 것을 곧장 깨닫게 되었지만.

“지금! 지금이다!”

“발시(發矢)!”

그 순간, 어느덧 협곡 안을 가득 메운 유목민들은 들을 수 있었다.

아득한 허공 위, 양옆으로 우뚝 선 험준한 절벽 위에서 울려 퍼진 누군가의 힘찬 외침을.

그리고 모두의 머리 위로 한 겹 덧씌워지는 어둠을.

솨아아아아.

스산한 파도 소리가 들렸다. 흐릿했던 달빛마저 지워 낸 수많은 화살들이, 협곡 전체를 뒤덮으며 내리꽂히고 있었다.

“저, 전원 방패……!”

그러나 비명처럼 터져 나온 누군가의 외침은 덧없이 파묻혔다.

카카캉!

암벽과 부딪친 화살촉 끝에서 피어오른 불똥.

느려진 세상 속, 마찰로 일어난 그 찰나의 흐릿한 불빛 사이로 피를 흩뿌리며 쓰러지는 수많은 인마가 비춰지고 있었다.

쐐액, 푸푸푸푸푹!

거센 파공성을 들었을 때는 이미 늦었다.

삼십여 장에 달하는 높이에서 직사(直射)로 내리꽂힌 강철의 비는 유목민들의 각궁을 뛰어넘는 위력으로 사방을 적셨다.

검붉은 피로. 고통에 찬 비명으로.

크아아악!

히히힝!

누구의 것인지도 모를 거대한 비명의 덩어리가 협곡을 가득 메웠다.

본능에 따라 무심코 고개를 들어 위를 바라보고 있던 유목민은 눈알에 꽂힌 화살을 부여잡고 뒹굴었고, 초원마는 주인의 안위조차 잊은 채 온 힘을 다해 몸부림쳤으며, 질긴 가죽 방패를 들어 목숨을 구한 운 좋은 백인장은 홀로 안도의 한숨을 내쉬었다.

그리고 그 한숨이 끝나기도 전에, 머리 위에서 울려 퍼지는 불길한 소리를 들었다.

구궁. 드드득.

‘천둥?’

아니, 틀렸다.

순간 머릿속을 스쳐 지나간 의문의 답을, 그는 얼마 지나지 않아 자신의 두 눈으로 직접 확인할 수 있었다.

“허.”

공허한 탄식.

쿵.

힘이 풀린 손아귀에서 고슴도치가 된 방패가 미끄러졌지만, 중년의 백인장은 조금도 신경 쓰지 않았다.

앞서 자신의 목숨을 구해 주었던 이 방패로도, 어둠 속에서 들이닥치는 저 거대한 것들을 막아 낼 수 없다는 사실을 이미 알고 있었으니까.

구구구구궁!

어둠 속, 지축을 울리며 암반을 타고 쏟아져 내리는 검은색의 구체들.

강철의 비가 그치기 무섭게 들이닥친 암석의 벼락 앞에서, 백인장은 문득 달빛마저 비추지 않는 하늘을 바라보았다.

“……텡그리시여.”

콰아아아앙!

돌아오지 않는 대답과 함께, 그의 하늘이 닫혔다.



* * *



- 이거, 위험한 거 아닙니까?

턱을 긁적이며 묻는 칭겐을 향해, 자무카는 담담한 신색으로 입술을 달싹였다.

- 몇이나 투입했지?

- 백인대 다섯, 여섯 정도?

칭겐이 입맛을 다시며 덧붙였다.

- 물론, 지금은 없어졌지만요.

불과 한 식경.

오백이 넘는 병력이 증발하기까지 걸린 시간이다.

그것도 제대로 된 전투를 시작해 보기도 전에.

그들의 적들은 생각했던 것 이상의 활약을 보여주는 중이었다.

- 그놈, 제법이더군요.

저 한마디가 누구를 가리키는 것인지, 자무카 역시 알고 있었다. 그는 조용히 고개를 끄덕였다.

- 검귀(劍鬼)의 자질이 보이더군. 네놈처럼.

- 선봉대를 전멸시킨 것도 저놈의 소행이 분명합니다.

- 그래서, 탐이 나나?

- 만약 제가 청한다면, 보내 주시렵니까?

칭겐의 눈빛이 붉게 번들거렸다.

말똥 냄새 풀풀 풍기는 게르에서 보낸 세월만 몇 년이었나. 오랜만에 맡은 먹잇감의 냄새에 피가 끓어오른 그의 모습에, 자무카는 작게 혀를 찼다.

- 아직 젊군. 그 나이에도 제 버릇을 못 버린 걸 보면.

- 대답을 못 들었습니다만.

- 지금 해 주지. 불가(不可).

- 이런.

칭겐이 미간을 찌푸린 그때, 자무카가 말을 이었다.

- 실망할 필요 없다. 먹잇감은 다른 곳에도 있으니.

- 그 말씀은…….

- 절벽 위를 점령해라. 워낙 성가시게 구니 더 늦기 전에 정리할 필요가 있겠지.

- 그것 참, 탁월한 선택이십니다.

칭겐은 환하게 웃었다.

그리고 저 높은 절벽 위에서 자신을 기다리고 있을 먹잇감들을 향해 걸음을 옮겼다.
```

## Final English reading copy

```markdown
# Chapter 956

Eight Spring Gorge was a little over a hundred *jang* long.

A natural gateway surrounded by towering cliffs some thirty *jang* high.

Its narrow width—barely enough for thirty grown men to stand shoulder to shoulder—made it the worst possible place to attack. But there was a reason two great battles with Shanxi Province’s fate at stake had been fought in this jar-shaped gorge.

“Break through! Trample them and keep going!”

“Brothers of the Great Steppe! Once we cross this godforsaken gorge, Shanxi Province will be ours!”

Eight Spring Gorge was the greatest strategic stronghold in the Shanxi region.

It was the quickest route through the rugged mountains covering the north, and the last passage leading to the central plains.

If they took this place, positioned on the border between north and central Shanxi, nothing would remain to stop tens of thousands of cavalry charging side by side, shaking the earth beneath their hooves.

And even if something did stand in their way, they could simply trample it.

A wave could never be held back by a handful of sand and gravel.

That was precisely why the defenders had to stop the invaders before them, by any means necessary.

“Hold the line! Don’t give up a single step!”

“Proud people of Shanxi! Defend your homeland from these merciless barbarians!”

“Raaaaaah!”

Screams of defiance pierced the darkness and echoed through the gorge.

And amid the dense rain of arrows both armies loosed at each other, one streak of light moved with graceful ease, seemingly apart from everything else.

*Shing!*

Space split apart.

The dozen or so mounted warriors charging with the steppe nomads’ distinctive cries suddenly felt the wind.

Not just a wind brushing past their bodies, but a cold gust sweeping through them to their very cores.

“…Huh?”

Their eyes widened. Their vision wavered.

And then—

*Shhk.*

An eternal blackout, one that light would never pierce again.

*Fwoosh!*

Fountains of blood surged into the air. The things that had once been people and horses were severed into pieces and flung in every direction.

They flew on with the same force they’d charged with—

toward the enemies they had chosen as their first targets, but never reached alive.

*Crunch!*

Even the lightest of them had weighed hundreds of *geun* in life, some nearly a thousand.

Jin Mukyung calmly looked down at the enormous chunks of flesh, caked in dirt and blood, that had carved deep furrows as they slid to his feet.

More precisely, he looked at their impossibly clean cut surfaces—and the sword in his grasp.

*As sharp as ever. Almost unbelievable.*

Admiration flickered in Jin Mukyung’s eyes as he gazed at the blade, its cold edge gleaming even in the dark.

Only two days earlier, he’d felt the new sword’s excellence in battle against a thousand enemies. And yet he couldn’t help being surprised all over again.

He was, after all, a swordsman with a desire for fine blades.

*I wondered what was going on when he suddenly handed me a sword I’d never seen before. If I’d refused, I’d have regretted it for the rest of my life.*

To a martial artist, a cherished weapon was their closest friend and family.

But just before Jin Mukyung’s first campaign, as he was polishing his beloved sword, a sturdy old man came to see him. He dropped a long bundle of cloth in front of him and said:

*“Get rid of that one. Use this from today on. I forged it for you well in advance, Second Young Master.”*

At first, he’d thought the old man was out of his mind.

He was telling him to discard the sword he’d used for over ten years—the one his older brother Jin Wikyung had spent enough to tear out one of the pillars of the Jin Family of Taiyuan to make.

But when a sword appeared from between the folds of the cloth, and at last its gleaming white blade emerged naked from its scabbard, Jin Mukyung understood.

The lunatic old man standing before him was an outstanding artisan unlike any he’d ever seen.

An artisan with more than enough skill to forge a divine weapon.

*“You’ve got a good eye, judging by your face. That’s a relief. You look worthy of being its owner, at least.”*

*“What is this…?”*

*“Can’t you tell? It’s one of the finest things this old man has ever made, and I worked myself to the bone making it in my old age. I forged it from something that can rival Ten-Thousand-Year Cold Iron, so take good care of it.”*

The old man had left without hesitation after saying that. Jin Mukyung remained absorbed in his new sword for a long while, until one of the family retainers finally told him who the old man was.

*“Come to think of it, Second Young Master might not know. The Ironcraft Hall was newly established in our family while you were in secluded training.”*

*“The Ironcraft Hall? Then that old man was…”*

*“Yes. He’s Hall Master Jang Taebo, head of the Ironcraft Hall. In the past, he spent over thirty years as Guild Leader of the Ironcraft Guild.”*

*“……!”*

Even Jin Mukyung, who had devoted himself to martial arts at the Jin Family of Taiyuan and Heaven’s Gate Temple, knew of the Ironcraft Guild.

A place where the finest artisans in the world gathered.

A group so proud of its skill that it would never sell a weapon to someone who lacked the qualifications, no matter how much gold they offered.

The retainer didn’t know why Jang Taebo, who had reigned as the guild’s greatest artisan for decades, was now at the Jin Family of Taiyuan. But there was one thing he knew for certain.

*“I believe he formed a connection with the Third Young Master. So, around the time you entered secluded training, he reversed his retirement and joined our family.”*

*“Taekyung? That guy?”*

*“Yes. And somehow, Hall Master Jang brought a great many artisans who’d belonged to the Ironcraft Guild along with him. It was probably because of his old ties to them.”*

But there was something neither the retainer who’d given him that information nor Jin Mukyung, fresh out of secluded training, knew.

The artisans who had left everything behind and rushed to the Jin Family of Taiyuan had not been moved by loyalty at all.

What had brought even the old Master Artisans who’d left their forges before Jang Taebo back to work was the final gift of a great spiritual creature, one that had once swum in a deep river more than ten thousand *li* away.

The Water God Dragon.

The imugi had failed to become a dragon, never obtaining the dragon pearl, and had ultimately been corrupted by Dark Heaven. But with a young man’s help, it found eternal rest and left behind its sacred body.

An ingredient for working metal so rare that even a meteorite fallen from the heavens or Ten-Thousand-Year Cold Iron might pale in comparison—something no famous artisan could resist.

And, naturally, a considerable amount of it had secretly made its way to the Jin Family of Taiyuan.

Its flesh and blood, imbued with spiritual power over hundreds of years, had become elixirs in their own right. Its incredibly strong bones had been made into weapons, and its thick, sturdy tendons and muscles had become parts of armor.

Before long, the Water God Dragon’s remains had been worked into every corner of the Jin Family of Taiyuan.

Just as they were at this very moment.

*Whoosh!*

No matter how fine the net, how could it catch every minnow?

With their path blocked by Jin Mukyung alone, the steppe nomads had faltered at the sight of their comrades’ gruesome deaths. The arrows they loosed to keep the Jin forces at bay slipped between the government troops’ shields and struck a martial artist of the Jin Family of Taiyuan in the chest.

Or at least, that was what it looked like for a moment.

*Thunk!*

The arrow bounced away without force, its earlier, powerful whistle now seeming absurd.

The martial artist of the Jin Family, who had felt certain he’d been mortally wounded and had been about to scream, stared with wide eyes.

“Guh—huh?”

He blinked blankly, then finally remembered.

The thin something he’d strapped over his chest beneath his uniform, on the Lesser Family Head’s strict orders.

It was so light, and glimmered so strangely, that he couldn’t tell whether it was iron or leather.

And as soon as he remembered, he burst into loud laughter as if nothing had happened.

“You stupid barbarian bastards! You couldn’t hit our family dog shooting like that!”

“……!”

“……!”

The nomads, who had been ready to trample those weak Han Chinese, could only look at one another in dismay.

Their bows had the power to pierce most leather armor with ease. And now they were useless.

It was only natural for unease to spread at the thought that one of the grasslands’ greatest weapons had been taken away from them.

Of course, they soon realized that even that brief moment of unease was a luxury they couldn’t afford.

“Now! Now’s the time!”

“Loose!”

At that moment, the nomads who now filled the gorge heard a powerful shout from far above, high on the steep cliffs rising on either side.

Then darkness fell like another layer over their heads.

*Shhhhhhh.*

A bleak roar like the sound of waves filled the air. Countless arrows blotted out even the faint moonlight as they plunged down, covering the entire gorge.

“E-everyone, shields—!”

Someone’s cry burst out like a scream, then was swallowed without a trace.

*Clang-clang-clang!*

Sparks bloomed where arrowheads struck the cliffs.

In the slowed world, through that brief, hazy light born of friction, they could see countless men and horses collapsing, spattering blood.

*Whoosh—thud-thud-thud!*

By the time they heard the fierce whistle of arrows, it was already too late.

The steel rain plunging straight down from a height of thirty *jang* drenched everything in its path with a force that outdid the nomads’ composite bows.

With dark red blood. With cries of pain.

“Raaaaagh!”

“Neigh!”

A huge mass of screams, from no one in particular, filled the gorge.

A nomad who had raised his head to look up on instinct writhed on the ground, clutching the arrow stuck in his eye. A steppe horse thrashed with all its might, forgetting even its rider’s safety. And a lucky hundred-man commander who’d saved his life with a tough leather shield let out a relieved sigh.

Before that sigh had even ended, he heard an ominous sound above him.

*Rumble. Rrrrattle.*

*Thunder?*

No. Wrong.

He soon saw the answer to the question that had flashed through his mind.

“Ah.”

A hollow sigh.

*Thump.*

The porcupine of arrows that had been his shield slipped from his weakened grasp, but the middle-aged hundred-man commander didn’t care in the slightest.

He already knew that even the shield that had saved his life couldn’t stop the enormous things rushing at him through the darkness.

*Rrrrrumble!*

Black spheres poured down the rock face out of the darkness, shaking the earth as they came.

Just as the steel rain stopped, the avalanche of rocks came crashing down. The hundred-man commander glanced at the sky, where not even the moonlight could reach.

“……Tengri.”

*Ka-boom!*

With no answer, his sky closed over him.

* * *

*—Isn’t this dangerous?*

Jamukha moved his lips with a calm expression as Chinggen scratched his chin and asked.

*—How many did you send in?*

*—Five or six hundred-man companies?*

Chinggen smacked his lips, then added:

*—Though there aren’t any left now.*

A mere half an hour.

That was how long it took for more than five hundred troops to vanish.

And they hadn’t even had a proper chance to begin fighting.

Their enemies were performing better than expected.

*—That man’s quite something.*

Jamukha knew who Chinggen meant. He nodded quietly.

*—He has the makings of a Sword Demon. Just like you.*

*—He must have been the one who annihilated the vanguard, too.*

*—So, you want him?*

*—If I asked, would you let me have him?*

Chinggen’s eyes gleamed red.

How many years had he spent in a ger reeking of horse manure? At the scent of prey, his blood was boiling for the first time in ages. Jamukha clicked his tongue softly.

*—You’re still young. Even at your age, you haven’t managed to break that habit.*

*—I still haven’t heard your answer.*

*—I’ll give it to you now. No.*

*—What a shame.*

Chinggen frowned, and Jamukha continued.

*—No need to be disappointed. There’s prey elsewhere.*

*—You mean…*

*—Take the cliffs. They’re being a nuisance, so we should deal with them before any more time passes.*

*—Now that’s an excellent choice.*

Chinggen beamed.

Then he set off toward the prey waiting for him on the high cliffs.
```
