<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0528.txt",
      "sha256": "15f7d408cd8bfd178cef58f389127cfaf3888f4163479cda3f0afe2cfd64dfe4",
      "bytes": 12946
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3dddf04c22bfc8505772ad1023f2454131d1b6a25916857dcac34dc2f0bb6217",
      "bytes": 3481
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5b8a3b7691981a2eddad149a60ae832221992dfc29bdeef6f12d008e24a74515",
      "bytes": 168930
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "7d0ad8a46f121f5508bda6f97530c841e89bd270e7b7a743c8653c035e4fbd03",
      "bytes": 1070
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "e558752fb40ff9080628833382d67d05a33e3bc839a270e6c3face25fca417f5",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "44134e99000f12b4bca618fcff0c719193e9d34087cbef7fa912058399922e5b",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a82de3808968902a74ce671d93dd523484dd13866e2d1c92f1697e2b5044cdb3",
      "bytes": 1630
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "508cf0e32f88d9164a91efc91b8c2763ab8ae13692e13d2ea63316901d0ae747",
      "bytes": 811
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5055fd089787aa6ed7851e0569df53546ad0b97272966a57ddd5f2bcd686b8b4",
      "bytes": 158189
    }
  ],
  "estimated_tokens": 10767
}
-->

# Durable State Update — Chapter 528

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 528. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 528. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 528,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 528,
    "continuity_sources": [528],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions, with Taekyung receiving a constant stream of visitors seeking connections to him or the Jin Family of Taiyuan.",
    "Taekyung reached the system status Exhaustion after three days of handling visitors.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license."
  ],
  "continuity_sources": [
    527,
    526
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 527,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution and 미미보 as Mimi Step; retain footwork technique for 보법.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 쌀벌레 as Rice Weevil and 만두 벌레 as dumpling grub; retain the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 주화란    | **Ju Hwaran**      |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 진수 | **Jinsu** | Named budding talent who receives Taekyung's autograph. |
| 영웅건 | **hero headband** | Headwear contrasted with turbans. |
| 미미보 | **Mimi Step** | Snake-inspired footwork technique created by Cheongpung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 527
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, and the creator of the snake-inspired Mimi Step footwork technique.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 524
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 527
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 527
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 342
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, and Heo Jun was her uncle.

## Korean source

```text
＃528화



끼익.

초대받지 않은 손님의 정체를 깨닫기까지는 그리 오랜 시간이 걸리지 않았다.

문을 열고 들어오는 낯익은 얼굴을 확인한 나는 망설이지 않고 입을 열었다.

“야, 혁무진. 누가 거지 들여보내래.”

“잘 있었…… 이 빌어먹을 놈이 말하는 본새 보게.”

때가 꼬질꼬질한 얼굴로 환하게 웃던 궁기방이 인상을 팍 구겼다.

“사람이 기껏 시간 내서 들렀더니, 뭐가 어쩌고 어째?”

“거지한테 거지라고 한 건데. 무슨 문제라도?”

“네놈은 듣는 거지 기분 나쁜 건 생각 안 하나?”

“응. 단 한 순간도.”

“……사갈보다 더한 놈 같으니. 언젠가 십만 개방도에게 둘러싸여 매타작당하는 날이 올 거다.”

나는 어깨를 으쓱해 보였다.

“안 될걸. 이래 봬도 무림맹에서 꽤 귀중한 전력이라.”

“내 동냥 그릇에 대고 맹세하건대. 때가 오면 네놈부터 조질 거다.”

“그것도 괜찮지. 그때가 오면 이 전쟁이 끝났다는 거니까.”

“그 말, 진심이냐?”

“어, 약속.”

천연덕스럽게 대답하는 나를 말 없이 노려보던 궁기방이 눈에 힘을 풀었다. 어느새 입가에는 희미한 웃음이 맺혀 있다.

“제기랄. 전쟁은 이제 겨우 막 시작되었는데 벌써 끝내고 싶어지는군.”

“왜, 나 때리고 싶어서?”

궁기방이 피식 웃으며 고개를 저었다.

“나야 평생을 빌어먹을 팔자지만, 그 정도로 생각이 없는 놈은 아니다. 전쟁은 무슨 일이 있어도 일어나선 안 돼.”

“전공을 세워 영웅이 될 수도 있는데?”

“나 같은 거지가 영웅이 되어서 뭣 하려고?”

“오.”

우문현답이다.

애초에 질문 자체도 녀석을 생각을 알고 싶어서 던진 거긴 했지만. 나는 진심을 담아 박수를 쳐 주었다.

짝짝짝.

“뭐냐?”

“그냥. 우리 기방이 다 컸구나 싶어서. 그런 생각도 다 하는 걸 보면.”

“……사람을 도대체 어떻게 보는 거냐? 그리고 네놈은 나보다도 어린 주제에 뻔뻔하기 그지없군,”

“나이 처먹었다고 다 철들었으면 세상이 지금보다는 훨씬 살 만해졌겠지. 시간은 아무 노력 없이도 흘러가는 거니까.”

그런 의미에서 궁기방의 생각은 또래의 무림인치고 똑바로 잡혀 있는 것이 맞았다.

이곳은 21세기의 현대가 아니라 원초적인 약육강식(弱肉强食)의 법칙이 통용되는 무림.

당장 지금 하남을 가득 메운 무림인들이 모두 의협심 하나만으로 무림맹에 참여했다는 말랑말랑한 생각은 하지 않는 게 좋다.

‘젊은 놈들일수록 더 그렇고.’

한창 피가 끓어오르는 나이 아닌가.

아니, 마흔 줄에 접어든 중년의 무림인이라 해도 크게 다르지는 않다. 그들에게는 정마대전은 태어나기도 전에 벌어진 과거의 흔적에 불과하니까.

이처럼 전쟁을 겪지 않은 세대 중에서는 의협심보다는 공을 세워 영웅이 되겠다는 포부를 가진 자들이 적지 않았다.

오늘 하루만 살 것처럼 구는 낭인들은 물론, 소위 명문대파라 불리는 대문파나 세가의 문하 제자들도 그렇다.

‘시대도 그렇고, 무림이라는 사회 풍조상 어쩔 수는 없지만…….’

아무리 좋게 보려고 해도 내 시선에는 병신들로 보일 수밖에 없다.

더불어 그런 병신들보다 의협심으로 무림맹에 참여한 이들이 더 많다는 사실이 천만다행으로 느껴진다.

‘생각해 보면 내 주위에 있는 놈들도 꽤 멀쩡한 축에 속하지. 음.’

그런 생각을 하고 있을 때, 청풍의 신형이 뱀처럼 미끄러지더니 궁기방의 앞에 불쑥 나타났다.

스으으윽!

“으헉! 뭐여, 시부럴!”

“헤헤. 제가 새로 만든 보법인 미미보(美美步)예요. 정말 미미 같죠?”

“미미 같긴 개뿔이. 개 같아! 거지 같다고!”

궁기방의 비명에 혁무진이 세상에서 제일 행복한 표정을 지으며 말했다.

“청 소협. 나중에 그거 한 번만 더 해 주시면 안 됩니까?”

“와아! 그럼요! 당연히 되죠!”

“되긴 뭐가 돼! 절대 안 돼! 하지 마!”

“…….”

멀쩡하긴 시벌.

한자리에 모아 놓으면 이만큼 병신 같기도 쉽지 않다.

‘아, 머리 아파.’

지끈거리는 관자놀이를 문지른 나는 잠시 뒤로 미뤄 두었던 질문을 던졌다.

“그런데 찾아온 용건이 뭐야?”

궁기방이 경계 어린 눈빛으로 청풍을 힐끔거리며 대답했다.

“너와 청 소협을 만나고 싶어 하는 사람들이 몇 있다. 혹시나 하는 마음에 부탁이나 해 볼까 하고 들른 거다.”

“당연히 나 만나고 싶어하는 사람들이야 널리고 널렸지.”

“……재수 없지만, 딱히 반박을 못 하겠군.”

“그래서, 날 만나고 싶어 한다는 그 사람들이 누군데.”

한숨을 내쉰 궁기방이 말을 이었다.

“십봉룡(十鳳龍).”

“십봉룡이라면.”

“네가 아는 그 십봉룡이 맞다. 모두 모인 것은 아니고 그 절반 정도지만.”

그럼 당연히 그 십봉룡이겠지. 다른 십봉룡도 있나.

그리고 그 세 글자를 듣는 순간 이미 마음은 정해졌다. 나는 일말의 고민도 없이 대답했다.

“싫어. 걔들 만나서 뭐 하라고.”

“교분을 쌓는 거다. 후기지수들끼리 돈독한 관계를 유지하면 나쁠 건 없으니까.”

“그렇다고 딱히 좋을 것도 없어 보이는데. 그리고 후기지수는 무슨. 나를 너희랑 같은 급으로 보면 곤란하지.”

궁기방의 얼굴이 황당함으로 물들었다.

“……네놈은 어떻게 그토록 기분 나쁜 말을 당당하게 할 수 있는 거냐?”

“그야 누구나 아는 사실이니까.”

“아니, 그렇긴 한데…… 제기랄. 알았다. 그럼 청 소협은?”

씨알도 안 먹힐 것이라는 사실을 알아챈 궁기방이 재빨리 표적을 돌린다.

취리리릭.

주위에서 관심을 끈 채 어느덧 구렁이가 되어 버린 천년독각사, 미미를 유심히 관찰하고 있던 청풍이 뒤도 돌아보지 않고 대답했다.

“음. 안 갈래요.”

“청 소협을 위해 진수성찬을 차려 놨는데도?”

“아까 만두 먹어서 배불러요. 배고팠어도 안 갔을 것 같고요.”

“싸 가면 되지. 배고플 때 먹으면 되잖아.”

“글쎄요. 요새 통 입맛이 없어서.”

“뭐, 뭣이!”

궁기방이 칼이라도 맞은 표정으로 눈을 부릅떴다.

아니, 충격을 받은 건 나와 혁무진도 마찬가지였다.

‘미쳤나? 정말 미친 건가?’

‘조장님. 제가 잘못 들은 겁니까?’

‘아냐. 제대로 들은 거 맞아. 입맛이 없대.’

‘저 새끼 저거, 청 소협 아닙니다. 암천의 간자가 확실해요.’

‘설득력이…… 있어!’

허공에서 눈빛을 통해 들리지 않는 대화가 오고 간다.

그만큼 청풍의 돌발 발언은 모두에게 엄청난 충격을 주었다.

‘다른 사람도 아니고 청풍이 입맛이 없다니.’

이건 신 무림맹 창설만큼이나 놀라운 소식이다. 하지만 나를 비롯한 사람들의 놀라운 시선에도 청풍은 꿈쩍도 하지 않았다.

“어쨌든 전 괜찮아요. 은인이나 다녀오세요.”

“어? 어어. 아냐. 나도 안가.”

“그래요? 헤헤. 그럼 전 하던 거나 마저 할게요. 미미보에 보완해야 할 점이 좀 있는 것 같아서요.”

도대체 왜 저러는지는 몰라도, 한 가지는 확실한 것 같다.

시간이 흐르고, 주위의 상황이 달라지면서부터 청풍에게도 어떠한 변화가 시작되고 있다는 것.

‘저 녀석…….’

말없이 청풍을 바라보던 나는 궁기방을 향해 고개를 돌렸다.

“어쨌든 이만 가 봐.”

“으응. 그래야겠군. 이야기가 길어지는 바람에 약속한 시간에 늦었어.”

여전히 충격이 가시지 않은 눈빛으로 청풍을 힐끔거리던 궁기방이 몸을 돌리며 중얼거렸다.

“그나저나 많이 실망하겠군. 특히 주 소저는 엄청나게 기대하는 눈치였는데.”

“실망은 무슨. 어차피 십봉룡 중에 몇 명은 성라대연 때 봤고, 결국 지나가다가 한 번쯤은 다시 만나게 될…….”

퉁명스럽게 대꾸하던 나는 순간 멈칫했다. 궁기방이 마지막에 덧붙인 한마디가 머릿속을 꽉 채웠다.

“잠깐. 누구?”

“응? 뭘 말이냐?”

“아니, 마지막에 누가 엄청나게 기대하고 있다고 들었던 것 같은데.”

“아아. 주 소저?”

맞다. 잘못 들은 것이 아니다.

“주 소저가 혹시, 그…….”

“당연히 네가 알고 있는 그 주 소저지. 용봉표국의 소국주인 은비화(隱匕花) 주화란 소저 말이다.”

“……!”

한 가지 기억이 문득 뇌리에 떠오른다.

무림으로 치면 고작 두세 달 전의 일에 불과하지만 어째서인지 까마득하게 느껴지는 기억.

하지만 아이러니하게도 지나간 시간 중에서도 유독 또렷하게 남아 있는 기억이기도 했다.



‘오늘은 달이 참 밝네요.’



그래, 그날은 유난히도 달이 밝은 날이었다.

아니, 어쩌면 정말 밝았던 것은 달이 아니라 누군가의 얼굴이었을지도 모르겠다.

그때의 나는 달을 바라보고 있지 않았으니까.



‘진 대협.’

‘네, 주 소저.’

‘나, 잘할 수 있을까요?’



꽃이 핀 정원에 스며들던, 한 사람의 축축하고 황량한 목소리가 귓가에 울려 퍼지는 듯했다.

그때의 내가 뭐라고 대답했더라.

잠시 생각에 잠겨 있던 나는 멍하니 중얼거렸다.

“……못해도 괜찮습니다.”

“뭐? 뭐가 괜찮다고?”

나는 문득 상념에서 깨어났다.

은은하던 달빛도, 꽃내음과 목소리도 사라지고 눈앞에 어른거리던 누군가의 얼굴마저 흐트러졌다.

고개를 들자 보이는 것은, 코앞에서 어리둥절한 표정을 짓고 있는 궁기방 뿐이다.

나도 모르게 작게 한숨이 흘러나왔다.

“기방아.”

“으응?”

“넌 왜 이렇게 못생겼냐.”

“……?”

“미안하지만 진심이야. 아니, 사실 별로 미안하지도 않은 것 같아. 한창 좋았었는데.”

궁기방의 못생긴 얼굴이 와락 일그러졌다.

“이 자식이 그런데 아까부터 자꾸…….”

“됐고.”

나는 고개를 가로저으며 이어지려는 녀석의 말을 끊었다.

“가자.”

“뭐?”

“되묻지 말고 십봉룡인지 뭔지 만나러 가자고. 진수성찬 얘기 들었더니 갑자기 배고파져서 그래.”

“어, 어어?”

화내는 것도 잊은 채 눈만 껌뻑이던 궁기방이 황급히 고개를 끄덕였다.

“어어. 뭐, 그러지. 다들 환영할 거다.”

누가 환영하건 딱히 상관은 없다.

그냥, 그냥 뭐랄까.

‘오랜만에 한번 보고 싶어진 것뿐이지.’

그래. 그것뿐이다. 적천강과 관련해서 감사를 표할 일도 있으니 가야 할 이유는 합당하기 그지없다.

‘사람 된 도리라면 당연한 거지. 당연한 거야.’

그렇게 내심 중얼거린 나는 걸음을 옮겼다. 뒤에서 같이 가자는 궁기방의 외침이 시끄럽게 울려 퍼졌다.



* * *



삼 층으로 이루어진 객잔은 크고 화려했다. 돈푼깨나 있는 이들이 아니라면 드나들 수 없을 만한 큰 규모와 값비싼 가격을 자랑했고, 실제로도 그러했다.

그런 의미에서 보자면, 객잔의 최고층인 삼 층의 창가 자리를 차지한 삼남 일녀(三男一女)의 신분 역시 평범과는 거리가 멀다고 할 수 있었다.

“주 소저. 술 한 잔 받으시지요.”

“어허. 소저께서는 술을 그리 좋아하지 않으신다네. 그렇지 않습니까, 주 소저?”

윤기가 흐르는 비단 무복과 영웅건을 두른 미남자들은 알지 못했다.

눈앞의 여인, 은비화(隱庇華) 주화란이 지금 어떤 생각을 하고 있는지.

‘언제 오시는 거지?’

이미 주위에서 떠드는 말은 들려오지도 않았다.

언제부터인지는 몰라도 의자에 기댄 몸은 창가 쪽으로 쏠려 있었고, 눈은 자꾸만 반쯤 열린 창과 계단을 바쁘게 훑기 바빴다.

‘궁 소협이 호언장담하셨는데. 지금이라도 가 볼까?’

그리고 온갖 고민과 생각들이 꼬리와 꼬리를 물고 이어지던 바로 그 순간.

짤랑.

객잔의 문이 열리는 종소리와 함께, 주화란은 자리에서 벌떡 일어났다.
```

## Final English reading copy

```markdown
# Chapter 528

Creak.

It didn’t take long to realize who the uninvited guest was.

The moment I saw the familiar face open the door and walk in, I spoke without hesitation.

“Hey, Hyuk Mujin. Who told you to let a beggar in?”

“Have you been well—this damn bastard has quite the mouth on him.”

Gung Gibang, who had been grinning brightly despite his grimy face, scowled.

“I went out of my way to make time for you, and this is how you greet me?”

“I called a beggar a beggar. What’s the problem?”

“Don’t you ever think about how the beggar feels hearing that?”

“No. Not for a single second.”

“……You’re worse than a scorpion. One day, you’ll find yourself surrounded by a hundred thousand Beggars’ Sect disciples and beaten half to death.”

I shrugged.

“Not likely. I happen to be a pretty valuable asset to the Murim Alliance.”

“I swear on my begging bowl that when the time comes, you’ll be the first one I beat senseless.”

“That works too. It’ll mean the war is over by then.”

“You mean that?”

“Yeah. Promise.”

Gung Gibang glared at me in silence. Then the tension left his eyes, and a faint smile appeared at the corners of his mouth.

“Damn it. The war has barely begun, and I already want it to be over.”

“What, because you want to beat me up?”

Gung Gibang gave a quiet laugh and shook his head.

“I may be destined to beg for the rest of my life, but I’m not stupid enough to think that way. No matter what, war must never happen.”

“You could distinguish yourself in battle and become a hero.”

“What would a beggar like me do with being a hero?”

“Oh.”

That was a wise answer to a stupid question.

I had asked because I genuinely wanted to know what he thought, but I applauded him sincerely.

Clap, clap, clap.

“What are you doing?”

“Nothing. I was just thinking our Gibang has really grown up. You’re even having thoughts like that now.”

“……How the hell do you see me? And you’re younger than me, yet you’re unbelievably shameless.”

“If simply getting older made people mature, the world would be a much better place. Time passes without anyone having to make an effort.”

In that sense, Gung Gibang’s thinking really was remarkably sound for someone his age in Murim.

This wasn’t the modern world of the twenty-first century. This was Murim, where the primal law of the jungle held sway.

It was best not to entertain the softheaded notion that every martial artist filling Henan had joined the Murim Alliance solely out of a sense of chivalry.

*Especially the younger ones.*

They were at the age when their blood was running hottest, after all.

Actually, even middle-aged martial artists nearing forty weren’t all that different. To them, the Great Faction War was merely a trace of the past that had happened before they were born.

Among generations that had never experienced war, plenty of people dreamed less of chivalry than of distinguishing themselves and becoming heroes.

That included not only wandering martial artists who acted as though they lived only for today, but also disciples of the great sects and great families collectively known as prestigious major factions.

*The era is what it is, and Murim’s social climate doesn’t leave them much choice……*

But no matter how favorably I tried to look at them, they could only appear to me as fucking idiots.

It felt like a godsend that there were more people joining the Murim Alliance out of chivalry than idiots like that.

*Come to think of it, the people around me are pretty normal too. Hmm.*

Just then, Cheongpung’s figure slid forward like a snake and suddenly appeared in front of Gung Gibang.

Ssss—

“Agh! What the fuck?!”

“Hehe. This is the new footwork technique I made, Mimi Step. It really looks like Mimi, doesn’t it?”

“Like Mimi, my ass. It looks like a dog! Like a damn beggar!”

At Gung Gibang’s shriek, Hyuk Mujin spoke with the happiest expression in the world.

“Young Hero Cheongpung, could you do that one more time later?”

“Wow! Of course! Absolutely!”

“Absolutely not! Don’t do it!”

“……”

Normal, my ass.

It wasn’t easy to gather this many people in one place and have them look this fucking stupid.

*Ah, my head hurts.*

Rubbing my throbbing temple, I asked the question I had set aside for a moment.

“Anyway, why are you here?”

Gung Gibang glanced warily at Cheongpung before answering.

“There are a few people who want to meet you and Young Hero Cheongpung. I thought I’d stop by and ask, just in case.”

“Of course there are plenty of people who want to meet me.”

“……You’re obnoxious, but I can’t exactly argue with that.”

“So who are these people who want to meet me?”

Gung Gibang sighed before continuing.

“The Ten Dragons and Phoenixes.”

“If you mean the Ten Dragons and Phoenixes……”

“They’re the Ten Dragons and Phoenixes you know. They’re not all here—about half of them.”

Well, of course they were those Ten Dragons and Phoenixes. Was there another group with the same name?

The moment I heard those three words, I had already made up my mind. I answered without the slightest hesitation.

“No. What am I supposed to do meeting them?”

“Build a relationship. It can’t hurt for young prodigies to maintain a close relationship with one another.”

“It doesn’t seem like it would help much either. And don’t call me a young prodigy. It’d be a mistake to put me in the same class as you people.”

Gung Gibang’s face filled with disbelief.

“……How can you say something so offensive with such confidence?”

“Because it’s something everyone knows.”

“No, that’s true, but…… Damn it. Fine. What about Young Hero Cheongpung?”

Having realized that he had no chance of persuading me, Gung Gibang quickly shifted his target.

Sssssss—

Cheongpung had been closely observing Mimi, the Thousand-Year Poison Horned Snake, who had somehow turned into a giant snake while drawing everyone’s attention. Without even turning around, he answered.

“Hmm. I don’t want to go.”

“They prepared a lavish feast especially for you.”

“I ate dumplings earlier, so I’m full. I don’t think I would’ve gone even if I were hungry.”

“They can pack it up for you. You can eat it when you’re hungry.”

“I don’t know. I haven’t had much of an appetite lately.”

“What—what did you say?”

Gung Gibang stared at him with his eyes bulging, as if he had just been stabbed.

No, Hyuk Mujin and I were just as shocked.

*What the hell? Is he really insane?*

*Captain, did I hear that wrong?*

*No. You heard him correctly. He said he has no appetite.*

*That bastard isn’t Young Hero Cheongpung. He’s definitely a Dark Heaven spy.*

*……That’s disturbingly plausible!*

An inaudible conversation passed between us through our gazes in midair.

That was how shocking Cheongpung’s sudden statement was to everyone.

*Of all people, Cheongpung says he has no appetite?*

It was news as astonishing as the founding of the New Murim Alliance. Yet Cheongpung didn’t so much as flinch beneath the astonished stares of everyone around him.

“Anyway, I’m fine. You go ahead, Benefactor.”

“Huh? Uh, no. I’m not going either.”

“Really? Hehe. Then I’ll finish what I was doing. I think there are a few things I need to improve in Mimi Step.”

I had no idea why he was acting like that, but one thing was certain.

As time passed and the circumstances around him changed, some kind of change had begun in Cheongpung as well.

*That guy……*

I stared at Cheongpung in silence, then turned toward Gung Gibang.

“Anyway, you should get going.”

“Hmm. I suppose I should. We talked so long that I’m late for the time we agreed on.”

Gung Gibang glanced at Cheongpung, still looking stunned, then turned away and muttered.

“They’ll be pretty disappointed. Young Lady Ju in particular seemed terribly excited.”

“Why would she be disappointed? I’ve already met some of the Ten Dragons and Phoenixes at the Star-Array Grand Banquet, and sooner or later we’ll run into the others again while passing by—”

I stopped in the middle of my blunt reply.

The last thing Gung Gibang had said filled my mind.

“Wait. Who?”

“Huh? What are you talking about?”

“No, I thought I heard you say that someone was especially excited.”

“Oh. Young Lady Ju?”

That was right. I hadn’t misheard him.

“Could you mean, by any chance, that Young Lady Ju……?”

“Of course I mean the Young Lady Ju you know. Young Lady Ju Hwaran, the Young Bureau Head of the Yongbong Escort Bureau—the Dagger Hidden Flower.”

“……!”

A single memory suddenly surfaced in my mind.

By Murim reckoning, it had happened only two or three months ago, yet for some reason, it felt impossibly distant.

Ironically, it was also one of the clearest memories left behind by all that time.

*The moon is especially bright tonight.*

Yes. The moon had been unusually bright that night.

Or perhaps it hadn’t been the moon that was truly bright. Perhaps it had been someone’s face.

I hadn’t been looking at the moon then.

*Great Hero Jin.*

*Yes, Young Lady Ju.*

*Do you think I can do it?*

It felt as though one person’s damp, desolate voice, drifting through the flower-filled garden, were echoing in my ears.

What had I said to her back then?

I thought for a moment before muttering blankly,

“……It’s all right even if you can’t.”

“What? What’s all right?”

I suddenly came to my senses.

The soft moonlight, the scent of flowers, and the voice had vanished. Even the face that had been flickering before my eyes dissolved.

When I looked up, the only thing in front of me was Gung Gibang wearing a puzzled expression.

A small sigh escaped me before I realized it.

“Gibang.”

“Hmm?”

“Why are you so ugly?”

“……?”

“I’m sorry, but I mean it. Actually, I don’t think I’m all that sorry. Things were going so well.”

Gung Gibang’s ugly face twisted violently.

“You bastard, you’ve been at it since earlier—”

“Enough.”

I cut him off with a shake of my head.

“Let’s go.”

“What?”

“Stop asking questions and let’s go meet those Ten Dragons and Phoenixes or whatever. Hearing about the feast suddenly made me hungry.”

“Uh, uh-huh?”

Gung Gibang blinked, having forgotten to be angry, then hurriedly nodded.

“Uh-huh. All right, then. They’ll all be happy to see you.”

It didn’t particularly matter who welcomed me.

It was just…… well, how should I put it?

*I just felt like seeing her after all this time.*

That was all. Besides, I had every legitimate reason to go, since I had something to thank her for concerning Jeok Cheongang.

*It’s only natural, if I’m a decent human being. It’s only natural.*

Muttering that to myself, I started walking. Gung Gibang’s shout that he was coming with me rang noisily from behind.

* * *

The three-story inn was large and ornate. Its scale and prices were enough to keep out anyone without a fair bit of money, and in reality, that was exactly how it was.

By the same token, the status of the three men and one woman occupying a window seat on the inn’s top floor was likewise anything but ordinary.

“Young Lady Ju, allow me to pour you a drink.”

“Now, now. Young Lady doesn’t care much for alcohol. Isn’t that right, Young Lady Ju?”

The handsome men, dressed in gleaming silk martial uniforms and hero headbands, had no idea what the woman before them was thinking.

*When is he coming?*

The words being thrown around her no longer reached her ears.

She didn’t know when it had begun, but her body, which had been leaning against the back of her chair, had gradually tilted toward the window. Her eyes kept sweeping restlessly between the half-open window and the stairs.

*Young Hero Gung made such a bold promise. Should I go out and see for myself?*

And just as all those worries and thoughts began chasing one another in endless circles—

Jingle.

The bell above the inn’s door rang as it opened, and Ju Hwaran sprang to her feet.
```
