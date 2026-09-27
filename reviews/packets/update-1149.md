<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1149.txt",
      "sha256": "064227bcc8099b5e83e5bf03f57d17730bc91bc78b77a03dc75db9d227311c24",
      "bytes": 11693
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7f38868bc80701554b15e6dbecd9c44bc5def696186dad42184871dfb5cf3e10",
      "bytes": 1621
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0c2c7c8b822a21edbf9fb8abda1956727086529d31a31ad49049d85289419fe9",
      "bytes": 246139
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ba4f40f99d96d37b185f257a30f93ead5c12cd01a3154af4f6c76a84c3bb1bc3",
      "bytes": 760
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "0b92aa89fed5e9de25296092f17f6c4696f06b997beaefd03193d7ff4673dec7",
      "bytes": 867
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "7f3579af86a77281c5bf9b7ac57eb65d0c29e96a98e8a0a6f5e502121e722cf7",
      "bytes": 619
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bf7859ae1f94bc4cd95e13e452647f001d596b267e8e1a51602d9cd5390de154",
      "bytes": 292059
    }
  ],
  "estimated_tokens": 8229
}
-->

# Durable State Update — Chapter 1149

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
1 and safe_through 1149. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1149. Profile updates may replace only one
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
  "chapter": 1149,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1149,
    "continuity_sources": [1149],
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
    "Taekyung has awakened at the bomb shelter battlefield, where Choi Minwoo leads over two hundred Hunters against monsters, including named foes with exceptional durability and regeneration.",
    "Taekyung and the much stronger Skeleton King are reunited allies and friends.",
    "The Grand Mage, reborn through the Lord of Heaven’s grace, rains destruction on the monsters; Taekyung recognizes her as his friend.",
    "The coalition army of over two hundred thousand is crossing the Taklamakan Desert toward Tianshan. Jeok Cheongang stays beside Taekyung to protect him; Taekyung promised he would return.",
    "The Grand Mage previously felt a wave. The Lord of Heaven said the heavens had opened again as green light rose over jade."
  ],
  "continuity_sources": [
    1147,
    1148
  ],
  "open_questions": [
    "What caused the wave the Grand Mage felt, and what did the Lord of Heaven mean by the heavens opening again?",
    "What danger awaits the coalition army at Tianshan?",
    "Who are the named monsters, and what accounts for their durability and regeneration?"
  ],
  "safe_through": 1148,
  "temporary_decisions": [
    "Render 仙界 as “realm of immortals” and 塔克拉玛干 as “Taklamakan Desert.”",
    "Render 스켈레톤 킹 as “Skeleton King,” 방공호 as “bomb shelter,” and 스톤 킹 as “Stone King” in the Skeleton King’s joking self-reference.",
    "Render 오러 as “Auror” and 검기 as “Sword Energy.”",
    "Render 리자드맨 as “Lizardman,” distinct from 리자드 (“Charmeleon”)."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 기루     | **pleasure house**                               |                                                       |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 육체파 | **physical school** | Taekyung’s joking self-description. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1148
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1143
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1148
- **Aliases:** None
- **Role:** A senior Dark Heaven sorcerer who directs its mages and participates in its plans to conquer the world.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** Cutting and sardonic, using taunts and pointed questions to challenge others.
- **Relationships:** Serves the Lord of Heaven and is an antagonistic peer of the Blood Lord, whose unilateral decisions anger her.

## Korean source

```text
＃1149화



전투가 마무리되기까지는 그리 긴 시간이 필요하지 않았다.

이미 우두머리 격이었던 일곱 마리의 네임드 몬스터가 대부분 죽거나 무력화된 시점부터 전황은 크게 기울었던 상황.

거기에 더해 인류가 보유한 최고의 워 메이지(War Mage)는, 등장과 함께 몬스터 군단의 산소호흡기를 박살 내 버렸다.

콰과과과광!

수십 미터 상공에서 쉴 새 없이 내리꽂히는 공격 마법에 땅거죽이 뒤집히고 핏물이 터져 나온다.

마치 저격이라도 하는 것처럼 완벽에 가까운 명중률.

전투는 그렇게 끝났다.

그 뒤에 이어진 행위는, 그저 일방적인 학살이었으니까.

“돌격! 모조리 섬멸해라!”

콰드드득!

나와 스켈레톤 킹, 그리고 최 팀장을 중심으로 파도처럼 나아간 삼백여 명의 헌터는 열 배가 넘는 적들을 집어삼켰다.

서걱, 푸푸푹!

나는 시야에 들어오는 적들을 닥치는 대로 베고 찔렀다.

제힘을 믿고 끝까지 저항하는 중대형 몬스터는 물론, 그제야 겁을 먹고 등을 돌려 도망치는 놈들까지도.

예외도, 자비도 없었다.

그렇게 삼십여 분 남짓한 추격과 학살의 시간이 지나자, 피로 뒤덮인 이 사막 위에 두 발로 서 있는 몬스터는 단 한 마리도 존재하지 않았다.

음.

사실, 한 마리 정도는 있긴 했다.

“다행히 우리 쪽 사상자는 없…… 뭐냐, 인간. 그 불손한 눈빛은?”

다가오려다가 말고 멈칫하는 스켈레톤 킹의 모습에, 나는 슬쩍 고개를 돌렸다.

“음. 별거 아냐.”

“충분히 별거 같은데.”

“예외는 어디에나 있는 법이지. 안 그래?”

“갑자기?”

“그런 게 있어. 너랑은 관계없으니까 더 캐묻지 마.”

수상쩍은 낌새를 눈치챘는지 녀석의 눈매가 가늘어졌지만, 다행히도 추가 심문을 받는 상황은 벌어지지 않았다.

태양을 등진 누군가의 커다란 그림자가, 마치 구원의 동아줄처럼 내 머리 위로 드리워졌으니까.

“거기 신사분들. 한 가지 묻고 싶은 게 있는데.”

다크 초콜릿처럼 거무스름한 피부와 커다란 근육. 거기에 더해 어지간한 근접 무기보다도 흉악하게 생겨 먹은 스태프(Staff)까지.

천천히 허공에서 내려온 거구의 대마도사는 떨리는 음성으로 말을 이었다.

“지금 내가 보고 있는 게, 빌어먹을 신기루나 환영 마법은 아니겠지?”

믿을 수 없다는 눈빛으로 이쪽을 응시하는 그를 향해, 나는 천천히 주먹을 내밀며 대답했다.

“글쎄요, 확인해 보실래요?”

“오, 제기랄. 진?”

미국의 대마도사, 매직 존슨(Magic Johnson)은 주먹 인사 대신 나를 와락 끌어안았다.

꾸욱.

“…….”

지금 이 순간 배를 찌르고 있는 단단하면서도 묵직한 무언가는, 아마도 그의 스태프일 것이다.

반드시 그래야만 한다.



* * *



매직 존슨이 흥분을 가라앉히기까지는 상당한 시간이 필요했고, 다행히도 그가 느낀 흥분은 오로지 재회의 기쁨에서 비롯된 것이었다.

그래. 아무리 흑인이어도 그 정도 크기와 강도는 말이 안 되지.

“신이시여. 보면서도 믿을 수가 없군. 도대체 언제 깨어난 거야?”

이제야 겨우 평정심을 되찾아가는 매직 존슨의 말에, 이 육체파 대마도사의 거대한 품 안에서 가까스로 탈출한 내가 대답했다.

본능적으로 그의 허리춤에 꽂힌 스태프를 곁눈질하면서.

“얼마 안 됐어요. 아직 실감이 잘 안 될 정도로.”

“아, 그렇군. 마지막으로 연락이 닿았을 때만 해도 네가 깨어났다는 소식은 듣지 못했으니까.”

“네?”

매직 존슨의 말에 담겨있는 그 묘한 표현에, 나는 애써 억누르고 있던 불길함이 마음속에서 꿈틀거리는 것을 느꼈다.

바로 이곳, 현대가 어떤 세상인가.

이제는 지구촌이라는 단어조차 부족할 만큼 현세의 인류는 눈부신 번영을 이루었다.

기존에 보유했던 최첨단 기술에 마법이라는 이능(異能)까지 더해졌으니, 대격변의 잿더미 속에서 새롭게 재탄생한 문명은 인류 역사상 그 어느 때보다 찬란하게 빛날 수밖에 없었다.

그런데…….

‘마지막으로 연락이 닿았을 때, 라고?’

일순간 그 말에 담긴 뜻을 쉽사리 이해할 수 없었다.

매직 존슨은 대마도사다.

수십억 인류 중 셋, 아니 이제는 둘밖에 없는 마법의 대가.

비록 워 메이지라는 특성상 그의 마법 대부분이 전투와 연관된 것이라고는 하나, 대마도사는 상상을 현실로 뒤바꾸는 존재다.

공간 이동 마법 한 번으로 수백. 혹은 수천 킬로미터를 뛰어넘기도 하고, 조건만 갖춰진다면 그와 비슷한 거리에 있는 누군가에게도 언제든지 연락을 취할 수 있는.

그렇기에 지금 매직 존슨이 쓴 표현은 내게 있어 이상한 것을 넘어 불길하기까지 했다.

그토록 위대하다는 대마도사가 맛이 간 통신장비로 간신히 아군과 연락한 통신병처럼 말하고 있었으니까.

그리고 이와 같은 일련의 상황은, 내 귓가에 한 가지 사실을 속삭이고 있었다.

마침내 현실을 마주할 때가 왔다고.

“존슨.”

“응?”

“그 마지막 연락이, 도대체 언제였죠?”

“그건…….”

문득 말꼬리를 흐린 매직 존슨이, 그제야 뭔가를 깨달았는지 곁에 있던 스켈레톤 킹을 향해 고개를 돌렸다.

“혹시?”

많은 의미가 담긴 그 짧은 물음에, 녀석이 변명처럼 중얼거렸다.

“젠장. 말해 줄 시간이 없었어.”

“……빌어먹을.”

“말해 줄 수도 없었고.”

정확히는, 나 역시 차마 묻지 못했다.

그만큼 두려웠으니까. 무서웠으니까.

‘도대체.’

도대체 그동안 무슨 일이, 어느 정도의 시간이 흐른 것일까.

나는 조용히 떨리는 숨을 내뱉었고, 그런 내 모습에 매직 존슨은 깊은 한숨을 토해냈다.

“Fuck.”

말해야 하는 이도, 들어야 하는 이도 고통스러운 상황.

하지만 미룰수록 고통만 커질 뿐이다.

“말해 주세요. 지금 당장.”

그리고 바로 다음 순간. 기다렸던 대답이 돌아왔다. 매직 존슨의 어깨 넘어에서.

“하루 전, 정확히는 21시간 전이었습니다. 마지막 연락은.”

최 팀장, 그다.

몬스터의 피와 살점이 덕지덕지 말라붙은 갑옷과 검이, 그 무엇보다 모래알처럼 바싹 메마른 그의 눈빛이 송곳처럼 시야에 틀어박혔다.

“첫 번째 연락은 그로부터 세 시간 전이었고요.”

24시간. 하루.

최 팀장의 입술 사이로 흘러나온 그 숫자가, 수천 배의 무게로 불어나 내 가슴을 짓누르고.

매직 존슨이 몬스터들을 향해 쏟아내던 그 모든 섬광을 합친 것보다 새하얗게 시야를 물들인다.

‘말도 안 돼.’

지금까지의 시간 배율을 아득하게 초월하는 시차.

하지만 이뿐만이 아니다.

최 팀장의 목소리가 들려오기도 전에, 나는 이미 본능적으로 깨닫고 있었다.

더욱더 잔인한 진실이 기다리고 있음을.

“그리고.”

사방을 짓누르는 거대한 정적 속, 크게 심호흡한 최 팀장이 이내 떨리는 음성으로 말을 이었다.

“오늘은, 당신이 의식을 잃은 지 열흘째 되는 날이었습니다.”

“……!”

그 순간.

두두둥.

음산하리만치 낮게 울려 퍼지는 전고(戰鼓)의 북소리와 함께, 무림에서는 볼 수 없었던 새로운 형태의 시스템 창이 눈앞에 떠올랐다.



- 메인 퀘스트, [격변]의 실패로 인해 트리거가 발동합니다.

- 임무 : 소환 저지 (실패)

- 당신은 [“최후의 심연” 도플갱어]를 처치했으나, 해당 임무는 달성하지 못했습니다.

- 메인 퀘스트 실패의 여파로 [마계]의 경계가 일부 개방되었습니다. 지금껏 알려지지 않은 미지의 존재들이 이 세상을 침범하고 있습니다.

- [균열]이 진행 중입니다. 진행도는 특정 조건을 만족할 시 변동되며, 시스템을 통해 확인할 수 있습니다.



현대에서의 마지막 기억 속에 또렷하게 남아있던 내용들.

그러나 그 위로 새롭게 덧씌워진 새로운 홀로그램 창에는, 지금껏 본 적도 들은 적도 없는 존재의 이름이 적혀 있었다.



- 알려지지 않은 미지의 존재가 기꺼이 소환에 응합니다.

- [흑룡공(黑龍公) 모르고스]의 거대한 그림자가, 이 세상에 드리워졌습니다.

- 새로운 메인 퀘스트, [균열과 붕괴]를 확인하시겠습니까?



석상처럼 굳어 있던 나는, 불현듯 떠올렸다.

무림에서의 마지막 밤, 의미 모를 악몽 속에서 보았던 그 거대한 날개를.

어둠에 잠긴 하늘을 떨어 울리던 용의 포효를.



* * *



실로, 칠흑(漆黑) 같은 사내였다.

종아리까지 닿을 만큼 긴 머리카락은 물론, 흑요석을 박아넣은 것 같은 두 눈동자까지.

그나마 사내가 가진 것 중 유일하게 다른 색을 지닌 것은 동공을 둘러싼 홍채(虹彩)뿐이었는데, 새하얀 것을 넘어 은색으로 빛나는 그것은 보는 이로 하여금 빨려 들어가는 듯한 감각을 느끼게 할 정도로 매혹적이었다.

물론, 침착한 눈빛으로 지금 막 자신의 집무실에 들어선 사내를 바라보고 있는 노인에게는 해당되지 않는 이야기였지만.

저벅. 저벅.

정적 속에서 울려 퍼지는 걸음 소리.

길게 뻗은 융단을 가로지른 사내가 코앞까지 다가온 뒤에야, 노인이 불쑥 입을 열었다.

“예의가 없군.”

대답 대신 돌아온 사내의 눈빛에, 노인이 재차 말을 이었다.

“손님이라면 신발은 털고 들어와야지. 융단이 더럽혀졌잖나.”

“아.”

사내의 입술 사이로 흘러나온 나지막한 탄성에, 노인은 가슴 한구석이 울렁이는 듯한 기분을 느꼈다.

아마도 사내의 발걸음을 따라 이곳저곳에 떨어진 인간의 피와 살 조각이 아니었다면, 그에게 무한한 호감을 표했을지도 몰랐다.

“미안하군. 아직 이런 것에는 조금 서툴러서.”

부드럽게 웃은 사내가 노인을 향해 손을 내밀었다.

그가 앞서 했던 말과는 달리, 매우 자연스러운 움직임으로.

“아, 혹시 이번에도 잘못한 건가? 이것이 너희들의 방식이라고 들었는데.”

고개를 갸우뚱하는 사내의 모습에, 잠시 침묵하던 노인이 대답했다.

“아니, 너무 능숙해서 놀랐을 뿐일세. 겉모습도, 방금의 그 악수도.”

자연스러운 것을 넘어, 기품과 우아함마저 깃든 움직임.

그리고…… 세상에서 가장 아름다운 인간이라 해도 과언이 아닌 겉모습까지.

하지만 노인은 알고 있었다.

심지어 그 두 눈으로 똑똑히 지켜보기까지 했다.

눈앞의 사내가, 불과 10여 분 전 단 한 번의 손짓으로 그가 사랑하는 붉은 광장을 지워버리는 것을.

“그래, 모르고스(Morgoth). 이곳에는 무슨 일로 왔나.”

러시아의 독재자, 블라디미르 푸린(Vladimir Purin)은 인간의 탈을 뒤집어쓴 괴물의 손을 맞잡으며 이를 악물었다.
```

## Final English reading copy

```markdown
# Chapter 1149

The battle didn’t take long to wrap up.

By the time most of the seven named monsters—the ones who’d been acting as leaders—were dead or incapacitated, the tide had already turned sharply in our favor.

On top of that, humanity’s greatest War Mage had appeared and immediately pulled the plug on the monster army’s life support.

KWA-BOOOOM!

Spells rained down without pause from dozens of meters above us, turning over the earth and sending blood spraying everywhere.

His accuracy was almost perfect, as if he were sniping his targets.

And so the battle ended.

What followed was nothing more than a one-sided massacre.

“Charge! Wipe them all out!”

CRUNCH!

With me, the Skeleton King, and Team Leader Choi at the center, some three hundred Hunters advanced like a wave, swallowing up enemies more than ten times their number.

Slash, splatter!

I cut and stabbed at every enemy that came into view.

The medium and large monsters that trusted their strength and fought to the end—and even the ones who had only just gotten scared and turned their backs to run.

No exceptions. No mercy.

After about thirty minutes of pursuit and slaughter, there wasn’t a single monster still standing on two feet in this blood-soaked desert.

Well.

Actually, there was one.

“Thankfully, we didn’t suffer any casualties… What’s that insolent look for, human?”

The Skeleton King had started toward me, then hesitated and stopped. I glanced over at him.

“Hmm. It’s nothing.”

“Looks like something to me.”

“There are exceptions to every rule. Right?”

“Where’d that come from?”

“It’s a thing. It has nothing to do with you, so don’t ask.”

He narrowed his eyes, apparently picking up on something suspicious, but thankfully I wasn’t subjected to any further interrogation.

A massive shadow, cast by someone standing with the sun at their back, fell over my head like a lifeline from heaven.

“Good gentlemen. I have a question for you.”

Dark-brown skin like dark chocolate. Muscles that strained the imagination. And on top of that, a staff that looked more vicious than most close-combat weapons.

The huge Grand Mage slowly descended from the air and continued in a trembling voice.

“What I’m looking at right now isn’t some damn mirage or illusion spell, is it?”

He stared at me with disbelieving eyes. I slowly held out a fist and answered.

“Why don’t you check?”

“Oh, damn it. Jin?”

Magic Johnson, the Grand Mage of the United States, pulled me into a tight hug instead of bumping fists.

Squeeze.

“……”

The firm, heavy thing poking me in the stomach right now was probably his staff.

It had to be.

* * *

It took Magic Johnson quite a while to calm down. Fortunately, all that excitement had come from the joy of seeing me again.

Yeah. No matter how black he was, no one could be that big and that hard.

“Dear God. I can’t believe it, even with my own eyes. When did you wake up?”

Magic Johnson had only just begun to regain his composure. I’d barely managed to escape the massive embrace of the Grand Mage, a man of the physical school, before answering.

I instinctively glanced at the staff tucked into his belt.

“Not long ago. I can barely believe it myself.”

“Ah, I see. The last time I managed to get in touch, I still hadn’t heard you’d woken up.”

“What?”

At that peculiar choice of words, I felt the foreboding I’d been struggling to suppress begin to stir inside me.

What kind of world was this modern one, anyway?

Humanity had flourished so brilliantly that even the word *global community* no longer seemed big enough to describe it.

They’d added Magic, a supernatural power, to the most advanced technology they already possessed. It was only natural that civilization, reborn from the ashes of the Great Cataclysm, would shine more brightly than at any other time in human history.

And yet…

*The last time he managed to get in touch?*

For a moment, I couldn’t make sense of what those words meant.

Magic Johnson was a Grand Mage.

One of only three masters of Magic among billions of people—or, now, one of only two.

As a War Mage, most of his Magic was related to combat, but a Grand Mage was someone who could turn imagination into reality.

With a single teleportation spell, he could cross hundreds—or even thousands—of kilometers. And if the conditions were right, he could contact someone just as far away whenever he wanted.

So what he’d said was more than strange. It was downright ominous.

He sounded like a signalman barely managing to contact his allies with a busted communications device.

And all of this was whispering the same thing in my ear.

That it was finally time to face reality.

“Johnson.”

“Yeah?”

“When was that last contact?”

“Well…”

Magic Johnson trailed off. Only then, as if he’d realized something, did he turn toward the Skeleton King beside him.

“Could it be…?”

The Skeleton King muttered like he was trying to defend himself.

“Damn it. I didn’t have time to tell you.”

“……Shit.”

“I couldn’t have told you, either.”

More precisely, I hadn’t been able to bring myself to ask.

I’d been that afraid. That scared.

*How long?*

What had happened while I was gone? How much time had passed?

I let out a quiet, trembling breath. At the sight of me, Magic Johnson heaved a deep sigh.

“Fuck.”

It was a painful situation for the one who had to speak and the one who had to listen.

But the longer we put it off, the more it would hurt.

“Tell me. Right now.”

And the very next moment, the answer I’d been waiting for came from over Magic Johnson’s shoulder.

“The last contact was one day ago—exactly twenty-one hours ago.”

It was Team Leader Choi.

His armor and sword were caked in dried monster blood and flesh, and his eyes were as dry as sand. They drove into my vision like awls.

“The first contact was three hours before that.”

Twenty-four hours. One day.

The number slipping through Team Leader Choi’s lips swelled to a weight thousands of times heavier, crushing my chest.

It washed my vision white, brighter than all the flashes Magic Johnson had unleashed at the monsters combined.

*No way.*

A time difference that dwarfed every ratio we’d seen so far.

But that wasn’t all.

Even before Team Leader Choi spoke, I’d already sensed it instinctively.

A far crueler truth was waiting.

“And…”

In the vast silence pressing down on us from every direction, Team Leader Choi took a deep breath. Then, his voice trembling, he continued.

“Today is the tenth day since you lost consciousness.”

“……!”

At that moment—

BOOM.

Along with the ominous, low rumble of a war drum, a new kind of System window—one I’d never seen in Murim—appeared before my eyes.

> **System**
> The trigger has been activated due to the failure of Main Quest Cataclysm.
>
> **Mission:** Prevent the Summoning (Failed)
>
> You defeated the “The Final Abyss” Doppelganger, but failed to complete the mission.
>
> As a consequence of the Main Quest failure, the boundaries of the Demon Realm have partially opened. Unknown beings, never before known to exist, are invading this world.
>
> A rift is in progress. Its progress will change when certain conditions are met and can be checked through the System.

The words were the same ones that had been etched clearly in my last memory of the modern world.

But over them, on a new holographic window, was a name for a being I’d never seen or heard of before.

> **System**
> An unknown being willingly answers the summoning.
>
> The immense shadow of Black Dragon Duke Morgoth[^1] has fallen over this world.
>
> Would you like to view the new Main Quest, Rift and Collapse?

I stood frozen like a statue, then suddenly remembered.

The enormous wings I’d seen in that meaningless nightmare on my last night in Murim.

The dragon’s roar, shaking the sky swallowed by darkness.

* * *

He was, in truth, a man of utter darkness.

His hair fell all the way to his calves, and his eyes looked as if they’d been set with obsidian.

The only part of him that wasn’t black was the irises around his pupils. They shone silver—brighter than white—and were so captivating they seemed to draw the viewer in.

At least, that was how they might have affected someone other than the old man looking back at the man who had just entered his office, his gaze calm.

Step. Step.

Footsteps rang out through the silence.

Only after the man had crossed the long carpet and come right up to him did the old man abruptly speak.

“You have no manners.”

In response to the man’s gaze, the old man continued.

“If you’re a guest, you should wipe your shoes before coming in. You’ve dirtied the carpet.”

“Ah.”

At the quiet exclamation that slipped from the man’s lips, the old man felt something stir deep in his chest.

If it weren’t for the bits of human flesh and blood scattered here and there along the man’s path, he might have felt boundless affection for him.

“My apologies. I’m still a little clumsy with things like this.”

The man smiled gently and held out his hand.

His movement was perfectly natural, despite what he’d just said.

“Ah, did I get it wrong again? I was told this is how you do things.”

The old man paused for a moment at the man’s puzzled tilt of the head, then answered.

“No. I was only surprised by how skilled you were. Your appearance—and that handshake just now.”

The gesture had been more than natural. It was graceful, even elegant.

And his appearance was so beautiful he could be called the most beautiful human in the world.

But the old man knew the truth.

He had seen it with his own eyes.

A little over ten minutes earlier, the man before him had erased the Red Square he loved with a single gesture.

“So, Morgoth. What brings you here?”

Vladimir Furin, the Russian autocrat, gritted his teeth as he clasped the hand of the monster wearing a human face.

[^1]: “Duke” renders the noble title 公 in the name 黑龍公.
```
