<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1177.txt",
      "sha256": "43a4bbbd08f5bbf7ef2c0f94d4d5f7cf129d6abf71f0842cf9d34a4931c2235c",
      "bytes": 11908
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "56a37d056ae292994a1172506941eece89d02960ead870deeea21a569e2c6dfe",
      "bytes": 1628
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6bd67da46d2a4fea774ad7ef64f30f16a650b1c6d85bd1a995fc818ad294b01a",
      "bytes": 248538
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "20e703f08f454cdd578f5fa19fecf0cd023aa9a1292b7f6c807fd24ea582db8f",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d5cfe144b6c598a671033e3ec44a70bacfc7b773cb016d7c4bb5bb02447ebd69",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "50fa5777d228499baf7dd5ef5d20d182f834f9baa61d58df98261b9e590960c4",
      "bytes": 1701
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1df348f7bbe89043d28753da52bd027dbceabfa4104532e5568759a2c330762c",
      "bytes": 295029
    }
  ],
  "estimated_tokens": 9012
}
-->

# Durable State Update — Chapter 1177

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
1 and safe_through 1177. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1177. Profile updates may replace only one
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
  "chapter": 1177,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1177,
    "continuity_sources": [1177],
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
    "Jin Taekyung has returned to Murim and reunited with Jeok Cheongang in Xinjiang.",
    "Nearly a month passed in Murim during Taekyung’s less-than-week-long absence in the modern world.",
    "Taekyung’s group is crossing the Taklamakan Desert; the land around them appears to contain no living things.",
    "Jin identifies the Lord of Heaven as the living Demon King Asmodeus, who caused the Great Cataclysm.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1176,
    1175
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why does the land around Taekyung’s group in Xinjiang contain no living things?",
    "Why is Cheon Taemin still alive despite the capsule’s stated permanent binding to its Player until death?"
  ],
  "safe_through": 1176,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1140
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1174
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1176
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

## Korean source

```text
＃1177화



죽음의 땅.

글자에 담긴 뜻 그대로, 온전한 사지(死地).

내가 미처 알아차리지 못한 그 진실은, 불현듯 목덜미에 맞닿은 칼날처럼 서늘하게 찾아왔다.

‘아무런 생명체도 없다니, 어떻게 이런 일이 가능하지?’

순간 본능적으로 뇌리에 떠오른 의문을 나는 이내 꾹 눌러 삼켰다.

어리석은 질문이다.

이 모든 것의 시작이자 끝에 서 있는 것이 천주(天主). 아니, 마왕 아스모데우스라면 더더욱 그렇다.

그저 상상으로만 존재하던 종말론을 현실로 끌어들인 존재.

놈의 정체를 깨달은 순간부터 이미 상식이라는 단어는 무의미해졌다.

그렇기에 다음 순간 빠르게 사라진 의문의 빈자리를 메운 것은 또 다른 의문이었다.

보다 현실적이고, 핵심에 맞닿아 있는.

그 흔한 새소리, 벌레 울음소리 하나 들려오지 않는 창밖을 말없이 노려보던 나는 문득 입을 열었다.

“무슨 목적일까요?”

어떻게, 를 논할 만한 시점은 한참 지났다.

지금의 내게, 우리에게 중요한 것은 이유다.

그리고 저 멀리서 불어온 모래바람 틈새에 숨어, 조금 전 마차 지붕 위에 자리 잡은 인기척의 주인 역시 그 사실을 알고 있는 듯했다.

“둘 중 하나겠지.”

소년처럼 앳된, 그러나 살아온 세월을 증명하듯 삭막함이 느껴지는 목소리로 살성(殺星)이 말을 이었다.

“첫 번째는 일전(一戰)이다. 신강 땅의 모든 것을 끌어모아 펼치는 마지막 일전.”

“그럼 두 번째는…….”

“정확히 어찌 된 영문인지는 모르나, 이 신강 땅 전체가 생명의 기운을 잃었다. 사람과 짐승은 발이 달렸으니 사라져도 그럴 수 있지만, 일대의 식물까지 모두 말라비틀어졌더군. 아마도 암천의 짓이겠지.”

적천강이 퉁명스러운 어조로 말을 받았다.

“쥐새끼처럼 엿듣고 있더니, 결국 하나 마나 한 얘기를 하는군.”

“말조심해. 혹시 아나. 당장 오늘 밤에 그 쥐새끼가 당신 목을 베어 버릴지도.”

“그거 나쁘지 않군그래. 그렇지 않아도 슬슬 식량이 떨어져 가는 마당인데, 내일 아침은 바싹 구운 쥐 고기가 좋겠어.”

“그놈의 말본새는 도무지 나아질 기미가 안 보이는군. 도대체 나이는 어디로 처먹는 거지?”

딱딱한 대꾸와 함께 창가로 드리워지는 그림자.

아무런 실체가 없는 유령처럼, 흡사 투과하듯 창문을 통해 마차 내부로 들어온 살성이 나를 응시했다.

마치 속에 감춰둔 것을 꿰뚫어 보듯이.

“그나저나 오래도 자더구나.”

나는 슬쩍 입맛을 다셨다.

살성과 동행한 지 제법 긴 시간이 흘렀지만, 무려 한 달을 떠나 있던 건 이번이 처음이다.

그리고 보통 사람의 상식에 의하면 한 달 내내 잠을 자는 인간은 세상에 존재하지 않는다.

하지만 어쩌겠나.

조만간 스스로 진실을 밝힐 날이 오겠지만, 지금 당장은 안면에 철판부터 깔아야지.

“예, 뭐. 제가 잠이 많은 편이라서.”

“아무리 그래도 한 달 동안 잠들어 있는 건 불가능할 텐데.”

“특이 체질이라서요.”

“강산이 다섯 번 바뀔 동안 천하를 떠돌며 온갖 환자를 만났지만, 그런 특이 체질은 존재하지 않아.”

“축하합니다. 오십 년 만에 새로운 특이 체질을 발견하셨네요.”

“…….”

“…….”

일순간 숨 막히는 정적이 마차 내부를 가득 채웠다.

살성은 물론 적천강까지 나를 미친놈 보듯이 바라본다.

하긴, 이건 의학적 지식까지 끌어올 필요도 없는 헛소리긴 했다.

“농담이고요. 사실 중간중간 몇 번 깨긴 했습니다. 기본적인 생리 활동, 뭐 그런 것도 해야 하잖습니까.”

“그건 몰랐군.”

“모르실 수밖에요. 스승님만 알고 계셨던 거라. 그렇죠?”

“으응?”

갑작스러운 도움 요청에 눈을 깜빡이던 적천강이 뒤통수를 긁적였다.

“어. 그게 그러니까, 흠.”

뭔가 반응이 이상하긴 했지만, 원래 거짓말을 할 때는 자연스러운 것이 제일 중요하다.

나는 살성이 이상함을 느낄 틈을 주지 않기 위해 빠르게 말을 이었다.

“며칠 전에도 한번 깼습니다. 하도 자다 보니까 오줌도 마렵고, 배도 고프더라고요.”

“며칠 전이라면 정확히 언제를 말하는 거지?”

“글……쎄요. 잠이 덜 깬 상태였어서 그것까진 잘 모르겠는데요.”

“그렇단 말이지.”

알겠다는 듯 고개를 끄덕인 살성이 혼잣말처럼 중얼거렸다.

“희한하군. 몇 번이나 깨는 동안 아무도 못 알아차렸다니.”

“그러게요. 참 희한하죠.”

“그보다 더 희한한 게 있는데, 뭔지 궁금하지 않으냐?”

살짝 공기가 탁해졌다고 느껴지는 건 단순히 기분 탓일까.

나는 왠지 모를 불안감 속에 고개를 내저었다.

“……아뇨. 딱히.”

“그럴 리가. 궁금할 텐데.”

“괜찮습니다. 가끔은 모르는 게 약일 때도 있는 거죠.”

“좋은 얘기야. 하지만 지금 상황에 가장 어울리는 말은 따로 있지.”

평소와 다른, 그래서 더 심상치 않게 느껴지는 부드러운 목소리로 살성이 덧붙였다.

“말이 매를 번다.”

“…….”

“어떻게 생각하느냐?”

어떻게 생각하긴 뭘 어떻게 생각해.

나는 억지 미소를 지으며 대답했다.

“엄청나게 궁금해지네요. 그 희한한 얘기가 뭔지 꼭 듣고 싶습니다.”

“사실 따로 놓고 보면 그리 대단한 이야기는 아니야. 정확히는, 내 입장에서는 꽤나 성가시고 귀찮은 일이었지.”

“무슨 말씀이신지…….”

“사제지간(師弟之間)의 정이 아주 두텁더군. 출발 첫날부터 매일 아침저녁으로 네 녀석의 상태를 살피지 않으면 어느 성질 더러운 늙은이가 난리를 치는 통에 단 하루도 조용할 날이 없었다.”

다시 떠올리는 것만으로도 피곤함이 밀려오는지, 착 가라앉은 눈빛으로 적천강을 노려본 살성이 말을 이었다.

“최근에는 그 지랄병이 극에 달했지. 한 달 가까이 깨어나지 않는 걸 보니 뭔가 문제가 생겼음이 분명한데, 왜 문제점을 발견하지 못하냐고 고래고래 소리를 지르더군.”

“…….”

“그게 불과 이틀 전이야. 더 할 말 있나?”

장난하나.

당연히 없지.

어째 좀 쎄하다 싶더라니, 아까 적천강의 반응이 이상했던 이유가 여기 있었구만.

살성에 더해 내 시선까지 받게 된 적천강이 창밖을 응시하며 중얼거렸다.

“아니, 뭐. 그렇게까지 소리를 지르진 않았는데…….”

“하다 하다 돌팔이라는 소리까지 들었지.”

“그렇게까지 직접적으로 비난하지도 않았고…….”

“그래, 다시 생각해 보니 조금 돌려서 말하긴 했군. 의술은 노름판에서 배웠냐고.”

“그런 말을 한 건 맞지만, 그리 심한 말은 아니지 않나…….”

“간만에 살성이라는 별호값 하려고 제자 죽인다는 소리는 도대체 어떤 생각으로 내뱉은 거지?”

“음. 그건 노부가 말이 좀 심하긴 했군. 자존심상 사과는 하기 싫고, 대신 심심한 유감을 표하지.”

장장 삼백여 년 동안이나 주기적으로 천하 무림인들을 꼴받게 만들었던 열화문의 정수(精髓)가 고스란히 녹아든 대답에 나도 모르게 탄성이 터져 나왔다.

정확히는, 그러려던 순간 살성의 표정을 보고 온 힘을 다해 참았다.

“이런 개씹……!”

나는 청풍이 이 자리에 없다는 사실에 매우 안도했다.

만약 녀석이 이 상황을 봤다면 ‘와, 고금제일의 살수가 쌍욕 박는 거 처음 봐요!’ 같은 헛소리를 지껄였을 테고, 그다음에는 바로 그 고금제일의 살수가 이성을 잃고 날뛰는 모습을 봐야만 했을 테니까.

하지만 다행히도 신의라는 또 다른 자아를 지닌 그는 내 친애하는 스승님과는 달리 최소한의 선을 지킬 줄 아는 사람이었고, 전직 살수답게 신기에 가까운 평정심 회복 스킬을 지니고 있었다.

“좋아, 그래……. 그럴 수 있지. 환자와 가까운 사람들은 종종 제대로 된 판단을 할 수 없으니까. 충분히 그럴 수 있어. 이해할 수 있어.”

자기 최면에 가까운 중얼거림과 함께 호흡을 가다듬은 살성이 나를 향해 고개를 돌렸다.

그러고, 나로서는 도저히 예상할 수 없었던 한 마디를 불쑥 내뱉었다.

“그래서, 그곳에서의 일은 잘 처리했느냐?”

“예?”

“네 고향 말이다. 듣기로는 선계(仙界)라고 했던가?”

“……!”

아주 잠깐, 세상이 멈춘 것 같았다.

계속해서 전해지는 마차의 덜컹거림과 창문 사이로 흘러드는 모래 알갱이, 마지막으로 다분히 작위적인 적천강의 헛기침 소리가 아니었다면 정말 그렇게 믿었을지도 모른다.

“크흠. 그렇게 됐다.”

그렇게 됐다. 그렇게 됐다. 그렇게 됐다…….

어느 심산유곡의 깊은 골짜기도 아닌데 메아리처럼 울려 퍼지는 그 음성에, 나는 잠시 눈을 감았다가 떴다.

그리고 애써 준엄한 얼굴을 하고 있는 적천강을 바라보았다.

아무런 말 없이, 지그시.

“왜, 왜 그리 보느냐.”

“…….”

“이게 그, 참. 노부로써도 어쩔 수 없었다. 네 녀석이 장장 한 달이나 자빠져 있으니 걱정도 되고, 살성 저놈이 하도 의심을 품기에…….”

“…….”

“조금, 아주 조금만 설명했다! 그래도 의원이 환자 상태에 대해 묻는데, 최소한 어느 정도는 알아야 할 것 아니냐!”

더듬더듬 변명하는 적천강의 모습에 나는 한숨을 푹 내쉬었다.

“알겠습니다.”

“길어야 며칠이면 깨어나던 놈이 이렇게 되다 보니 이쯤 되면 혹시 무슨 사마외도(邪魔外道)에서 흘러나온 몽혼약에 중독된 건 아닌가 싶기도 했……. 뭐라고?”

“알겠다고요. 그러실 수 있죠.”

뭐, 이렇게 된 이상 어쩔 수 없지.

나만의 생각일 수도 있지만 살성과도 제법 정이 쌓였고, 가장 든든한 아군 중 한 명이니까.

살성은 내 비밀을 알 자격이 있는 사람이다.

사실, 이렇게 되니 오히려 속 편한 마음도 없잖아 있다.

게다가 다른 누구도 아닌 스승인 적천강의 판단이었으니 그에게도 나름의 이유와 사정이 있었을 거다.

당장 나 같아도 적천강이 겨울잠 자는 곰처럼 한 달 내내 잠들어 있었다면 설마, 하는 마음이 들었을 테니.

그나저나…….

“저에 관한 이야기를 어디까지 말씀하신 겁니까?”

“음. 그게…….”

뭐지, 이 서늘한 느낌은.

부연 설명이라도 더 해줘야 하나 싶어서 물어본 건데, 적천강이 우물쭈물 눈치를 보며 말을 이었다.

“노부가 알고 있는 선에서는 대충 어느 정도 말했다. 처음에는 반응이 가지각색이긴 했는데 그래도 다 믿어 주더구나.”

“아, 그래도 괜찮습니다. 어차피 조만간 말할 생각이기도 했……. 잠깐, 가지각색이요?”

거 이상하네.

사람은 하난데, 왜 반응이 여러 개지.

순간 뇌리에 떠오른 의문은, 저 멀리서 들려온 외침과 함께 해결되었다.

“와아아아! 은인! 잘 다녀오셨어요?!”

아.
```

## Final English reading copy

```markdown
# Chapter 1177

A land of death.

Just as the words said, it was a place of utter death.

The truth I hadn’t noticed until then came upon me all at once, cold as a blade pressed to the back of my neck.

*How can there be no living things at all? How is this possible?*

The question sprang into my mind on instinct, but I quickly swallowed it down.

A foolish question.

If the Lord of Heaven—no, the Demon King Asmodeus—stood at the beginning and end of all this, then it was even less surprising.

The being who had dragged the apocalypse from the realm of imagination into reality.

From the moment I realized what he was, the word *common sense* had lost all meaning.

So the question that quickly took the place of the first was a different one.

A more practical question, closer to the heart of the matter.

I stared silently out the window at the empty landscape. Not a single bird called. Not an insect chirped. Then I spoke.

“What’s the purpose?”

It was far too late to ask how this could happen.

What mattered to me now—to us—was why.

And it seemed the person hiding in the sandstorm that had blown in from far away, whose presence had settled on the carriage roof a moment earlier, knew that too.

“Must be one of two things.”

The Slaughter Saint continued in a voice young enough to belong to a boy, yet bleak enough to betray the years he’d lived.

“The first is a final battle. One last fight, drawing on everything in Xinjiang.”

“Then the second is…”

“I don’t know exactly what’s happened, but this whole region has lost its life force. People and animals have legs, so it would make sense if they disappeared. But even every plant in the area has withered away. Dark Heaven’s probably behind it.”

Jeok Cheongang took up the conversation in a gruff tone.

“You were eavesdropping like a rat, and all you’ve got is something anyone could’ve said.”

“Watch your mouth. You never know. That rat might cut your throat tonight.”

“I wouldn’t mind. We’re running low on food anyway. A nice, crisp roast rat would make a fine breakfast tomorrow.”

“There’s no hope that way of talking will ever improve. What the hell happened to all the years you’ve lived?”

A shadow fell by the window as he answered flatly.

Like a ghost with no substance, the Slaughter Saint passed through the window as if it weren’t there and entered the carriage. He stared at me as though he could see straight through whatever I was hiding.

“Anyway, you slept a long time.”

I smacked my lips.

I’d been traveling with the Slaughter Saint for quite a while, but this was the first time I’d been away for a whole month.

And by ordinary standards, no one in the world could sleep for an entire month.

But what could I do?

The day would come when I’d tell him the truth myself. For now, though, I had to put on a straight face and bluff.

“Yeah, I’ve always been a heavy sleeper.”

“Even so, it’s impossible to stay asleep for a month.”

“I’ve got a special constitution.”

“I’ve wandered the land for fifty years, meeting all kinds of patients, and I’ve never encountered a constitution like that.”

“Congratulations. You’ve discovered a new one after fifty years.”

“…”

“…”

For a moment, suffocating silence filled the carriage.

The Slaughter Saint and even Jeok Cheongang stared at me as if I were a madman.

Fair enough. It was nonsense that didn’t even require medical knowledge to debunk.

“I’m kidding. Actually, I woke up a few times in between. You still have to take care of basic bodily functions and all that.”

“I didn’t know that.”

“You wouldn’t. Only my Master knew. Right?”

Jeok Cheongang blinked at my sudden plea for help, then scratched the back of his head.

“Uh. Well, that is…”

His reaction was a little odd, but when you’re lying, the important thing is to sound natural.

I quickly continued before the Slaughter Saint could notice anything strange.

“I woke up once a few days ago, too. After sleeping so long, I had to pee and got hungry.”

“When exactly do you mean by a few days ago?”

“Um… I wasn’t fully awake, so I’m not sure.”

“I see.”

The Slaughter Saint nodded as if he understood, then muttered to himself.

“Strange. You woke up several times, and nobody noticed.”

“Yeah. Weird, isn’t it?”

“There’s something even stranger. Want to know what it is?”

Was it just my imagination, or had the air gone a little stale?

I shook my head, uneasy for some reason.

“…No. Not particularly.”

“Surely you’re curious.”

“I’m fine. Sometimes it’s better not to know.”

“That’s a good saying. But there’s another one that fits this situation better.”

The Slaughter Saint added in a gentle voice unlike his usual one, which made it feel all the more ominous.

“Keep talking and you’ll get a beating.”

“…”

“What do you think?”

What do I think? What am I supposed to think?

I forced a smile and answered.

“I’m suddenly very curious. I’d love to hear this strange story.”

“On its own, it’s not that remarkable. To be exact, from my perspective, it was just a real nuisance.”

“What do you mean…?”

“Quite the bond between Master and Disciple. From the very first morning after we set out, that ill-tempered old man made a racket if I didn’t check on you every morning and evening. Not a single day went by in peace.”

The Slaughter Saint’s eyes sank as he glared at Jeok Cheongang, as though just remembering it exhausted him.

“Lately, his damn fits have gotten worse than ever. You hadn’t woken up in nearly a month, so it was obvious something was wrong. He kept yelling at me, demanding to know why I hadn’t found the problem.”

“…”

“That was just two days ago. Got anything to say?”

You’ve got to be kidding me.

Of course I don’t.

I’d thought something felt off. Now I knew why Jeok Cheongang had acted so strangely earlier.

With the Slaughter Saint’s eyes on him—and mine too—Jeok Cheongang stared out the window and muttered,

“Well, I didn’t yell quite that much…”

“He even called me a quack.”

“I didn’t insult you quite that directly…”

“Right. Now that I think about it, you did put it more gently. You asked if I’d learned medicine at a gambling den.”

“I did say that, but it wasn’t that harsh…”

“And what possessed you to accuse me of trying to live up to my title as the Slaughter Saint by killing your Disciple?”

“Hmm. I suppose I did go too far there. My pride won’t let me apologize, so I’ll offer my sincere regrets instead.”

The answer was steeped in the essence of the Fire Gate Clan—a clan that had been making Murim’s people furious on a regular basis for more than three hundred years. A sound almost escaped me.

Almost. Then I saw the Slaughter Saint’s expression and held it back with every bit of strength I had.

“You fucking—!”

I was very relieved Cheongpung wasn’t here.

If he’d seen this, he would’ve spouted some nonsense like, *Wow! I’ve never seen the greatest assassin of all time swear before!* Then I would’ve had to watch the greatest assassin of all time lose his temper and go on a rampage.

Fortunately, the man with another identity as the Divine Physician knew how to keep to a minimum standard of decency—unlike my dear Master—and, as a former assassin, had a near-supernatural skill for recovering his composure.

“Fine. Sure… I can understand that. People close to a patient sometimes can’t make sound judgments. That happens. I get it.”

After muttering as if trying to hypnotize himself, the Slaughter Saint took a steadying breath and turned to me.

Then, with a suddenness I could never have predicted, he blurted out a question.

“So, did you take care of things over there?”

“What?”

“Your hometown. I heard you called it the realm of immortals?”

“……!”

For just a moment, it felt as though the world had stopped.

If not for the carriage’s constant rattling, the sand slipping through the window, and Jeok Cheongang’s extremely deliberate clearing of his throat, I might’ve believed it had.

“Ahem. It came up.”

*It came up. It came up. It came up…*

His voice echoed like an echo, though we weren’t in some deep mountain valley. I closed my eyes for a moment, then opened them.

Jeok Cheongang was trying very hard to look stern.

I gazed at him in silence.

“W-why are you looking at me like that?”

“…”

“Well, I couldn’t help it. You’d been out cold for a whole month, and I was worried. The Slaughter Saint kept asking questions…”

“…”

“I explained a little. Just a little! He’s a physician. If he asks about a patient’s condition, shouldn’t he know at least something?”

I let out a long sigh at Jeok Cheongang’s halting excuses.

“Understood.”

“You used to wake up after a few days at most, but when you stayed out this long, I started wondering if you’d been poisoned by some kind of sleeping drug from the demonic, heterodox arts… What?”

“I said I understand. You had your reasons.”

Well, what was done was done.

Maybe it was just me, but I’d grown pretty close to the Slaughter Saint. He was one of my most dependable allies.

He deserved to know my secret.

Besides, the decision had been made by none other than my Master, Jeok Cheongang. He must’ve had his reasons and circumstances.

If Jeok Cheongang had slept for an entire month like a bear hibernating through winter, even I would’ve started to wonder.

Anyway…

“How much did you tell him about me?”

“Hmm. Well…”

Why did I suddenly feel so cold?

I’d only asked in case I needed to explain more, but Jeok Cheongang hesitated, glancing at me before continuing.

“I told him more or less what I knew. At first, their reactions varied, but they all believed me.”

“Oh, that’s fine. I was planning to tell you soon anyway… Wait, ‘their reactions’?”

That was strange.

There was only one of him. Why were there several reactions?

The question that flashed through my mind was answered by a shout from somewhere in the distance.

“Waaah! Benefactor! You’re back! Did you have a good trip?”

Ah.
```
