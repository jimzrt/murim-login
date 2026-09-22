<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0720.txt",
      "sha256": "005bac60aaff703c4974e5ba38ffb4bda8032744826ac72dbeef788d3bf4638e",
      "bytes": 12551
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5aa5ed2bf0321702d16505af86e8c263df539b7945bad558063556f73568fabc",
      "bytes": 1421
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91a3a66cd8c4494676c8e3729299c8ac8ec06db73a599c8c8a4efc8085c6d7d5",
      "bytes": 208479
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "1f07af8b77b909da50e215ed25d35a0578238248fc55a7cba983922e80b7305e",
      "bytes": 846
    },
    {
      "path": "characters/Guardian Spirit.md",
      "sha256": "f32807d61b0e10323aaad31616b297d5e0bd04b6201fa98173b2217e1e353389",
      "bytes": 645
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "50bc4df8f44adea62c158ec6331ae90f6fb3342148f70de5b69e495188a2334c",
      "bytes": 1702
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "1a35c391ae035095bc78c679a122624d9dff90c53bc5e66be91025a138e047ef",
      "bytes": 600
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "70a23c1d468d66fcffb8866ed68c3e39d0f659b769f18088b06c4bc39f31ccaf",
      "bytes": 676
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "4dd8bc33c49be103e1abca08cca2d785439bb60d6484373cea243d482e6a3e6d",
      "bytes": 659
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c9370e66f36ae1c5da9e5fb2bed205edcf0688392c7bf8f70a9318539923074",
      "bytes": 219239
    }
  ],
  "estimated_tokens": 9609
}
-->

# Durable State Update — Chapter 720

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 720. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 720. Profile updates may replace only one
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
  "chapter": 720,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 720,
    "continuity_sources": [720],
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
    "Jin Taekyung has accepted the Quest [Corrupted Divine Artifact].",
    "The corrupted divine artifact is the former sacred stone, now consumed by demonic qi and still being suppressed by the Beast Miao King.",
    "The Beast Miao King cannot suppress the artifact's demonic qi indefinitely.",
    "Jeok Cheongang proposed destroying the artifact, but Jin Taekyung stopped him because a failed destruction could cause another catastrophe.",
    "The guardian spirit's sacrifice to close the rift motivates Jin Taekyung to prevent the artifact from exploding.",
    "The Poisonblood Grounds and the Sacred Land are separate places.",
    "The Sacred Land is Nanman's heart and a land of life.",
    "Placing the corrupted artifact at the Sacred Land revealed a hidden radiant space and a brilliant pond.",
    "Jin Taekyung believes purification may create a new sacred stone."
  ],
  "continuity_sources": [
    719
  ],
  "open_questions": [
    "Will purification at the Sacred Land successfully create a new sacred stone?",
    "What will happen to the corrupted artifact and its demonic qi during purification?"
  ],
  "safe_through": 719,
  "temporary_decisions": [
    "Render 타락한 신물 as Corrupted Divine Artifact and 신석 as sacred stone.",
    "Render 정화 as Purification.",
    "Keep 독혈지 as Poisonblood Grounds and 성지 as Sacred Land."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 아문 | **Amun** | Acupoint |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |
| 수호령 | 적천강 | guardian_spirit_to_legendary_martial_master | old human | terse and contemptuous | The guardian spirit addresses Jeok as 늙은 인간 while recognizing that his essence has not changed. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |
| 적천강 | 야수묘왕 | senior allied martial master to Nanman Beast Palace Lord | you | blunt, commanding, and mocking | Jeok orders the Beast Miao King to stand aside and mocks his inability to destroy the corrupted artifact. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 719
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people who has resumed leadership of Nanman after the rift disaster.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Guardian Spirit.md

# Guardian Spirit (수호령)

- **Safe through:** Chapter 719
- **Aliases:** None
- **Role:** The Guardian Spirit was a divine-beast-like tiger that sacrificed itself to seal the rift and was killed after becoming corrupted.
- **Personality:** The Guardian Spirit was self-sacrificing and chose death rather than allow its corruption to continue.
- **Voice:** The Guardian Spirit communicates through roars and terse cries; no sustained speech is established.
- **Relationships:** The Guardian Spirit asked Jin Taekyung and Jeok Cheongang to kill it if corruption overcame it.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 719
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 719
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and is trusted by Jin Taekyung, who can ride and communicate with him.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 719
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit and protector of the land; after absorbing the sacred stone, it entered the rift to seal it despite the risk of corruption and death.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger shared a roughly three-hundred-year friendship with Yayul Cheon, once refused his request for aid, and now trusts Jin Taekyung and Jeok Cheongang to kill it if the rift corrupts it.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 719
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who returned to the Nanman Beast Palace with Jin Taekyung and voluntarily entered the underground prison after siding with Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃720화



후우.

선선한 바람이 느껴진다. 작게 심호흡한 나는 주위를 바라보았다.

성지(聖地).

그 두 글자가 이토록 어울리는 장소가 또 있을까.

하지만 내가 발을 딛고 선 이 자리는 몸통에 불과하다.

‘이런 성지조차, 심장은 따로 있지.’

생명과 정화의 기운이 가득한 곳.

이미 앞서 한 번 죽어 가던 내 몸뚱어리를 되살린 바로 그 장소.

나는 저 멀리 보이는 연못을 향해 천천히 걸음을 옮겼다.

태양이 없음에도 머리 위로 내리쬐는 빛은 따스하고, 온 사방에 흐드러지게 피어난 꽃과 풀은 싱그럽다.

아연한 표정으로 이 기이한 공간을 바라보던 적천강과 야수묘왕은 뭐라 말할 듯이 입술을 달싹였지만, 이내 굳게 입을 다문 채 내 뒤를 따랐다.

하지만 그런 그들의 인내심도 그리 오래가지는 못했다.

찰박.

거침없이 연못을 향해 걸음을 내딛자, 차가운 강물이 금세 허리까지 차올랐다. 그런 내 모습에 적천강이 경호성을 토해 냈다.

“저, 저 녀석이……!”

자결이라도 하는 줄 알았던 모양이다.

적천강은 당장이라도 내 멱살을 붙잡고 끌고 나올 기세였지만, 나는 가타부타 설명하는 대신 새끼손가락을 깨물었다.

으득.

희미한 고통과 함께 살이 갈라지고 피가 흐른다.

그러나 나는 눈을 부릅뜬 적천강을 향해 씩 웃어 보인 뒤, 망설임 없이 맑은 강물에 손을 담갔다.

‘일. 이. 삼…….’

마음속으로 느릿하게 숫자를 센 뒤 손을 빼자, 불과 삼십여 초 남짓한 시간 만에 완전히 아문 새끼손가락이 모습을 드러냈다.

당장이라도 강물에 뛰어들 것 같던 적천강도, 그런 그를 만류하던 야수묘왕도 이 믿을 수 없는 광경에 신음처럼 중얼거렸다.

“이게 무슨.”

“……요희가 한 말이 사실이었군. 전부 사실이었어.”

옛날 사람들이 백문이불여일견(百聞而不如一見)이라는 고사성어를 심심해서 만들었겠나.

역시 입 아프게 떠들어 봤자, 직접 보여 주는 게 빠른 법이다.

‘일종의 퍼포먼스지.’

다행히 이 퍼포먼스의 효과는 확실했고, 더불어 나 역시 한 가지 사실을 재확인할 수 있었다.

‘아직 효능이 남아 있어.’

솔직히 약간 걱정했다.

핵을 파괴당한 골렘이 와르르 무너지는 것처럼, 마기에 잠식당한 신석(神石)으로 인해 성지 역시 사라졌을까 봐.

하지만 그런 내 우려는 새끼손가락의 상처처럼 깨끗이 사라졌고, 그 빈자리를 채운 것은 확신에 가까운 짐작이었다.

‘이거였어, 정답이.’

시스템은 지금껏 단 한 번도 거짓말을 하지 않았다.

항상 있는 사실 그대로를 전달할 뿐이며, 그 단조롭기 그지없는 텍스트 속에서 새로운 길을 찾아내는 것은 오롯이 내 몫이었다.

바로 이번처럼.

‘퀘스트 정보란에는 어떤 방식으로든, 이라고 적혀 있었지. 분명히.’

맞다. 처음부터 내게 주어진 퀘스트 임무는 [타락한 신물]의 ‘처분’이지, ‘파괴’가 아니었다.

나는 그 의미를 비교적 뒤늦게 깨달았고, 수호령과 얽힌 기억 속에서 한 신비로운 장소를 떠올릴 수 있었다.

중태에 빠져 있던 내 몸을 치유하고, 몸속 노폐물을 정화시켜 주었던 어느 연못에 관한 기억을.

‘치유와 정화.’

저 근원을 알 수 없는 신비로운 효능이 어디에서 비롯되었는지는 모르나, 이 이상의 선택지는 없다.

나는 연못을 중심을 향해 걸음을 내디뎠다.

스륵.

잔잔한 물결이 나를 중심으로 퍼져나간다. 연못의 수심은 그리 깊지 않았고, 투명하리만치 맑은 수면에는 긴장감으로 굳어 있는 한 사람의 얼굴이 출렁이고 있었다.

꿀꺽.

마른침을 삼킨 나는 꽉 쥐어진 주먹을 바라보았다.

[타락한 신물]의 단단한 감촉과 함께, 손가락 사이로 울컥거리며 솟구치는 강대한 마기(魔氣)가 느껴진다.

‘……근데 이거, 잘못해서 역효과 나면 진짜 대환장 파티 시작인데.’

농담이 아니라 이 정도 마기라면 연못은 물론 성지까지 조져 버리고도 남는다.

그때는 진짜 찐 트루 독혈지가 되어 버릴 테고, 이제 막 저승 전입 신고를 끝마친 수호령이 매일 밤 꿈속에 등장해서 하악질을 해 대겠지.

하지만 뭐…….

‘나보고 어떡하라고. 이거 말고 별다른 선택지가 없는데.’

시바, 모르겠다.

눈을 질끈 감은 나는, 손에 쥔 [타락한 신석]을 곧장 물속으로 처박았다.

첨벙! 촤아아악!

잔잔하던 수면이 흩어지고 솟구친 물보라가 내 전신을 흠뻑 적신다.

그리고…… 온 사방이 고요해졌다.

“……?”

뭐야, 이거. 왜 이렇게 조용해.

억겁과도 같은 짧은 시간 속, 잠시 망설이던 나는 감았던 눈을 떴다.

살짝. 아주 살짝.

그리고 내가 조심스럽게 실눈을 뜬 그 순간.

부그르르.

수면 위로 올라오는 수포(水泡)와 함께.

쉬우우우우.

연못의 중심으로부터, 혼탁한 어둠과 뒤섞인 물살이 회오리쳤다.

그러니까 그 말인즉슨…….

‘시벌, 딱 여기네?’

한 줄기 깨달음과 동시에, 거대한 물의 기둥이 내 발아래에서 솟구쳐 올랐다.



* * *



콰아아아아!

반응할 틈도 없었다. 그저 사방이 물이었고, 어둠이었다.

대비할 틈도 없이 들이닥친 혼란 속에서 나는 있는 힘껏 몸부림쳤다. 아니, 몸부림치려 했다.

다음 순간, 비로소 현실을 깨닫지 않았다면 그러했을 것이다.

“……!”

똑똑히 보였고, 느꼈다.

나를 중심으로 힘차게 소용돌이치는 물살과 어둠을. 그리고 물 속이라면 느낄 수 없는 신선한 공기와 바람을.

‘공기? 바람?’

나는 눈을 깜빡이며 주위를 둘러보았다.

수면 속 부유감 따위는 느껴지지 않는다. 가슴께까지 차올랐던 물도 사라졌다.

발아래에는 단단한 지면이 있었고, 사방에는 물살과 어둠이 끝없이 소용돌이치고 있었다.

‘나를…… 감쌌다?’

틀림없다. 이 거대한 물의 기둥은 내 전신을 휩쓰는 대신 감싸 안았고 사방을 가로막은 어둠과 물결 너머에서는 있을 수도, 믿을 수도 없는 광경이 스쳐 지나가고 있었다.

촤아아아악!

‘이건.’

단번에 깨달을 수 있었다.

지금 내가 보고 있는 것은 극심한 혼란으로 인한 환각 증세, 그런 것 따위가 아니다. 이 연못에 담긴 어느 장소의 역사일 뿐이다.

아니, 탄생과 이 땅과 운명을 함께해 온 신물(神物)의 기억일지도 모른다.

“……신석(神石).”

신음처럼 중얼거린 나는 아연한 눈빛으로 사방을 가로막은 물의 기둥을 바라보았다.

쉼 없이 흐르는 물결 속에서는 아득한 시간도 함께 흐르고 있었다.

아무것도 없는 황폐한 땅에서 고개를 내민 새싹이 거목(巨木)으로 성장하고, 풀과 꽃이 자라나자 동물들이 하나둘씩 모습을 드러낸다.

‘빠르다.’

찰나라고도 부를 수 없는 짧은 시간 속, 물결에 비친 풍경은 끊임없이 변화했다.

눈 깜빡할 사이에 수십 번씩 뒤바뀌는 낮과 밤. 어느 날은 천둥과 번개가 온 세상을 가득 메우고, 또 어느 날은 산이 무너져 강을 지웠다.

수백. 혹은 수천 년.

하지만 변화무쌍하기 그지없는 이 긴 시간의 흐름 속에서도 신석은 오롯이 제 자리를 지켰고, 그런 신석의 곁을 지키는 존재들 역시 있었다.

말. 원숭이. 표범. 곰…….

종도. 생김새도 다른 짐승들. 그러나 감히 짐승이라 부를 수 없는 존재들.

그들은 밤하늘의 별처럼 수없이 빛났다가 사그라들었고, 이내 눈처럼 새하얀 한 마리의 백호가 신석을 지키기 시작했다.

‘수호령(守護靈).’

그리고 이내 어둠이 찾아왔다. 몸서리칠 만큼 끔찍한 어둠이, 끈적하고도 악한 기운이 물결 속에서 넘실거렸다.

긴 세월을 지나, 마침내 도달한 그 날의 기억.

하지만 마지막 수호령은 새하얀 갈기를 흩날리며 달려나갔다. 포효를 내지르며 어둠을 물어뜯고 할퀴었다.

전신 곳곳에 자리 잡은 상흔(傷痕)으로 마기가 스며들 때까지. 청백색의 눈동자가 검게 물들던 그 순간까지.

그리고 신석에 담긴 모든 기억도 함께 끝났다.

아니, 어쩌면 그것은 새로운 시작일지도 몰랐다.

스륵.

다시 한번 수면이 흔들린다. 어둠이 사라지고 사방을 휘감은 물의 기둥에 한 사람의 얼굴이 떠오른다.

눈을 질끈 감은 채 손에 쥔 무언가를 연못 깊숙이 담그고 있는 청년의 모습은, 모를 수 없을 만큼 익숙했다.

신석의 새로운 기억. 그 시작은 바로 나였고, 이는 한 가지 사실만을 의미했다.

띠링.

귓가를 파고드는 맑은 종소리와 함께, 물기둥 속에서 몸부림치던 어둠이 흔적도 없이 사그라들었다.

그 광경을 멍하니 지켜보던 내 눈앞에 반투명한 홀로그램 창이 떠올랐다.



- [생명의 연못]은 악하고 불순한 모든 기운을 정화합니다.

- [타락한 신물]에 스며 있던 [마기]가 완전히 사라집니다!

- 임무 : [타락한 신물] 처분 (완료)

- 퀘스트, [타락한 신물]을 성공적으로 완료했습니다!

- 퀘스트 완료 보상으로 막대한 경험치와 명성을 획득했습니다!

- 레벨 업!

- 레벨 업!

- 당신은 믿을 수 없는 업적을 달성했습니다!

.

.

띠링. 띠링. 띠링.

쉴 새 없이 울려 퍼지는 시스템 알림과 허공을 메우는 홀로그램 창들.

그러나 지금 나를 둘러싼 모든 것이 멀게만 느껴지는 이유는, 서서히 흩어지는 물기둥 사이에서 홀로 빛나고 있는 한 가지 물건 때문이었다.

슥.

홀린 듯 뻗은 손을 따라 물살이 갈라진다.

어린아이의 주먹보다 작고 가벼운, 하지만 믿을 수 없이 따스한 그것에 손끝이 닿은 그 순간.

화아아악!

눈부신 광휘가 부풀어 올랐다.

사방을 가로막고 있던 물기둥이 하늘 위로 솟구침과 동시에 폭발하듯 터져 나갔다.

촤아아아악!

숨겨진 성지를 넘어, 머나먼 어딘가로 끝없이 퍼져나가는 생명의 힘.

새로운 신석을 손에 쥔 나는 문득 고개를 젖혀 하늘을 바라보았다.

점점이 떨어져 내리는 물방울 사이로 다시 한번 맑은 종소리가 울려 퍼지고 있었다.

띠링.



- [생명의 연못]에 담긴 기운이 비가 되어 이 땅 곳곳에 스며듭니다.

- 땅은 더욱더 비옥해지고, 초목은 늘 푸를 것이며, 상처 입은 이들은 치유될 것입니다.

- [생명의 연못]이 모든 기운을 잃고 메말랐습니다. 하지만 걱정하지 마십시오. 시간에는 많은 것을 바꿀 수 있는 힘이 있습니다.

- [신석]은 지금까지 그러했듯 이 땅에 존재할 것입니다. 새로운 [수호령]과 함께.



새로운 수호령?

그 말의 의미를 깨닫기도 전에, 누군가의 발자국 소리가 귓가에 닿았다.

저벅.

이제는 더 이상 연못이라 부를 수 없는, 메마른 지면을 딛고 선 커다란 앞발.

어디선가 불어온 바람에 눈처럼 새하얀 터럭이 흩날리고, 한층 맑고 또렷해진 청백색의 눈동자는 기억 속 누군가를 쏙 닮아 있었다.

“……그래, 너구나.”

크르릉.

무야호. 아니, 새로운 수호령이 다가와 머리를 비빈다.

나는 말 없이 그런 녀석의 목덜미를 쓰다듬어 주었고, 넋 나간 얼굴로 이 모든 광경을 바라보던 적천강은 간신히 입술을 뗐다.

“……저놈, 노부가 데려가면 안 되겠느냐?”

순간 정색한 야수묘왕이 되물었다.

“되겠습니까?”

그들은 미처 알지 못했다. 자신들의 머리 위로 떨어져 내리고 있는 빗물에, 지금 막 푸른 잎사귀가 불쑥 고개를 내밀었다는 것을.

그리고 이 비가, 사흘에 걸쳐 남만 땅 전체를 적시리라는 것도.
```

## Final English reading copy

```markdown
# Chapter 720

Whew.

I could feel a cool breeze. After taking a small, deep breath, I looked around.

The Sacred Land.

Could there be another place where those two words fit so perfectly?

But the place where I stood was merely its body.

*Even a Sacred Land like this has a separate heart.*

A place filled with the energy of life and Purification.

The very place that had already brought my dying body back to life once before.

I slowly walked toward the pond in the distance.

Although there was no sun, the light shining down from above was warm, and the flowers and grass blooming wildly in every direction were fresh and vibrant.

Jeok Cheongang and the Beast Miao King stared at the bizarre space with stunned expressions. Their lips moved as though they were about to say something, but before long, they firmly shut their mouths and followed behind me.

However, their patience didn’t last very long.

Splash.

As I stepped straight toward the pond, the cold water quickly rose to my waist. Seeing me like that, Jeok Cheongang let out an alarmed shout.

“Th-that bastard…!”

He seemed to think I was about to kill myself.

Jeok Cheongang looked ready to grab me by the collar and drag me out at any moment, but instead of explaining myself, I bit down on my pinky finger.

Crack.

The flesh split, and blood flowed with a faint sting of pain.

But after giving the wide-eyed Jeok Cheongang a crooked grin, I plunged my hand into the clear water without hesitation.

*One. Two. Three…*

I slowly counted in my head before pulling my hand out.

In barely thirty seconds, my pinky had completely healed.

Even Jeok Cheongang, who had looked ready to leap into the pond, and the Beast Miao King, who had been trying to stop him, could only mutter like they were groaning in disbelief.

“What is this?”

“……What Yohi said was true. Every word of it.”

Do you think people in olden days came up with the saying that seeing something once was better than hearing about it a hundred times for no reason?

No matter how much you talked until your mouth went dry, showing someone directly was still faster.

*It was a kind of performance.*

Fortunately, the performance had worked perfectly. At the same time, I was able to confirm one more thing.

*It still works.*

To be honest, I had been a little worried.

Just as a Golem whose core had been destroyed would collapse into pieces, I had feared that the Sacred Land might have disappeared because of the sacred stone consumed by demonic qi.

But that concern vanished as cleanly as the wound on my pinky, replaced by a suspicion bordering on certainty.

*This is it. This is the answer.*

The System had never lied to me—not even once.

It only conveyed facts exactly as they were. Finding a new path within its maddeningly plain text was entirely up to me.

Just like this time.

*The Quest information said “by some means or another.” I’m sure of it.*

That was right. From the beginning, the mission I had been given was to *dispose of* the Corrupted Divine Artifact, not to *destroy* it.

I had realized the meaning relatively late, and the memories connected to the guardian spirit had reminded me of a mysterious place.

A pond that had healed my body when I was critically injured and purified the impurities within me.

*Healing and Purification.*

I didn’t know where those mysterious effects came from, but they had to be my only option.

I stepped toward the center of the pond.

Ssssh.

Gentle ripples spread outward from me. The pond wasn’t very deep, and on its surface—clear enough to see through—I could see the face of a man stiff with tension wavering in the water.

Gulp.

After swallowing my dry saliva, I looked down at my tightly clenched fist.

Along with the solid feel of the Corrupted Divine Artifact, I could sense powerful demonic qi surging up between my fingers.

*……But if this backfires, we’re in for a total shitshow.*

I wasn’t joking. With demonic qi this powerful, it would be more than enough to wreck not only the pond but the entire Sacred Land.

Then this place would become the real, true Poisonblood Grounds, and the guardian spirit—who had only just finished filing his move-in registration in the afterlife—would show up in my dreams every night and hiss at me.

But still…

*What am I supposed to do? I don’t have any other choice.*

Fuck it. I don’t know.

I squeezed my eyes shut and plunged the Corrupted Sacred Stone in my hand straight into the water.

Splash! Fwoosh!

The calm surface scattered, and a spray of water shot up and soaked my entire body.

And then…the surroundings fell silent.

“……?”

What the hell? Why was it so quiet?

After hesitating for a moment in that brief span of time that felt like an eternity, I opened my eyes.

Just a little. Very carefully.

And at the moment I cautiously peered through narrowed eyes—

Blub blub.

Bubbles rose to the surface.

Whoooooosh.

From the center of the pond, water mixed with murky darkness began to whirl into a vortex.

Which meant…

*Fuck, so this is it?*

At the same time as that realization struck me, a gigantic pillar of water surged up from beneath my feet.

* * *

Kwaaaaaaah!

There wasn’t even time to react.

There was only water and darkness in every direction.

Caught in the chaos that had rushed upon me without warning, I thrashed about with all my strength.

No—I tried to.

That was what I would have done if I hadn’t realized the truth in the next moment.

“……!”

I saw it clearly, and I felt it.

The water and darkness swirling violently around me. The fresh air and wind that I shouldn’t have been able to feel underwater.

*Air? Wind?*

I blinked and looked around.

I no longer felt any sensation of floating beneath the surface. The water that had risen to my chest was gone as well.

There was solid ground beneath my feet, while water and darkness continued to swirl endlessly in every direction.

*It…surrounded me?*

There was no doubt. Instead of sweeping across my entire body, the enormous pillar of water had enclosed me. Beyond the darkness and waves blocking me in on every side, impossible and unbelievable scenes flashed past my eyes.

Fwoooosh!

*This is…*

I understood immediately.

What I was seeing wasn’t a hallucination caused by extreme confusion or anything of the sort. It was simply the history of some place contained within this pond.

No. It might have been the memories of the divine artifact that had shared this land’s fate since its birth.

“……Sacred stone.”

I muttered the words like a groan and gazed with stunned eyes at the column of water walling me in on every side.

Within the ceaselessly flowing water, an impossibly distant span of time was flowing as well.

On a barren land where nothing existed, a sprout pushed its way up and grew into a great tree. Once grass and flowers began to grow, animals appeared one after another.

*It’s fast.*

Within a span of time too short to even be called an instant, the scenery reflected in the waves changed without pause.

Day and night switched places dozens of times in the blink of an eye. One day, thunder and lightning filled the entire world. On another, a mountain collapsed and erased a river.

Hundreds. Perhaps thousands of years.

Yet even amid the endlessly changing flow of time, the sacred stone remained exactly where it was. There were also beings that stayed by its side.

Horses. Monkeys. Leopards. Bears…

Animals of different species and appearances. And yet, they were beings that could hardly be called animals.

Countless among them shone like stars in the night sky before fading away, and eventually, a snow-white White Tiger began guarding the sacred stone.

*The guardian spirit.*

Then darkness arrived.

A horrifying darkness that made the body shudder. A sticky, wicked energy undulated through the waves.

The memory of that day, reached after the passage of a long age.

But the final guardian spirit charged forward, its white mane flying behind it. It tore into and clawed at the darkness with a roar.

Until demonic qi seeped through the scars covering its body.

Until the moment its blue-white eyes turned black.

And then every memory contained within the sacred stone ended as well.

No. Perhaps it was a new beginning.

Ssssh.

The surface rippled once more.

The darkness vanished, and a man’s face appeared within the pillar of water coiling around me.

The figure of a young man with his eyes squeezed shut as he immersed something in his hand deep into the pond was unmistakably familiar.

A new memory of the sacred stone.

Its beginning was me, and that meant only one thing.

Ding.

Along with the clear chime that pierced my ears, the darkness writhing within the pillar of water faded away without a trace.

As I stared blankly at the sight, a translucent holographic window appeared before me.

> **System**
>
> - Pond of Life purifies all evil and impure energy.
>
> - The demonic qi that had seeped into the Corrupted Divine Artifact has completely disappeared!
>
> - Mission: Dispose of Corrupted Divine Artifact (Complete)
>
> - You have successfully completed the Quest, Corrupted Divine Artifact!
>
> - You have obtained a vast amount of EXP and Fame as a Quest completion Reward!
>
> - Level Up!
>
> - Level Up!
>
> - You have accomplished an unbelievable achievement!
>
> …
>
> …
>
> …

Ding. Ding. Ding.

System notifications rang out without pause, and holographic windows filled the air around me.

But the reason everything surrounding me felt so distant was the single object shining alone through the slowly dispersing column of water.

Ssssh.

The water parted along the path of my hand as I reached out as though entranced.

The moment my fingertips touched it—something smaller and lighter than a child’s fist, yet unbelievably warm—

Fwoooooosh!

Dazzling radiance swelled outward.

At the same time, the column of water walling me in on every side shot into the sky and burst apart like an explosion.

Fwooooooosh!

The power of life spread endlessly beyond the hidden Sacred Land, toward some faraway place.

Holding the new sacred stone in my hand, I suddenly tipped my head back and looked at the sky.

Another clear chime rang out amid the droplets falling all around me.

Ding.

> **System**
>
> - The energy contained within the Pond of Life becomes rain and seeps into every corner of this land.
>
> - The earth will become even more fertile, the plants will remain evergreen, and the wounded will be healed.
>
> - The Pond of Life has lost all its energy and dried up. But do not worry. Time possesses the power to change many things.
>
> - The Sacred Stone will continue to exist in this land, just as it has until now. Together with a new guardian spirit.

A new guardian spirit?

Before I could understand what those words meant, the sound of someone’s footsteps reached my ears.

Thud.

A large forepaw stepped onto the parched ground that could no longer be called a pond.

Snow-white fur fluttered in a breeze that had come from somewhere, and the blue-white eyes, now clearer and more distinct, looked exactly like those of someone from my memories.

“……So it’s you.”

Grrrr.

Muyaho.

No—the new guardian spirit approached and rubbed its head against me.

Without saying a word, I stroked the back of its neck. Jeok Cheongang, who had watched the entire scene with a dazed expression, barely managed to part his lips.

“……Could this old man take that one with him?”

The Beast Miao King immediately asked with a stern expression.

“Would that be possible?”

They didn’t know.

They didn’t know that a green leaf had just poked its head out beneath the rain falling on them.

Nor did they know that this rain would soak the entire land of Nanman for three days.
```
